import os.path
import sys

from PyQt6.QtCore import QObject
from StdioBridge.client import Client
from TestGeneratorPluginLib import Plugin
from TestGeneratorPluginLib._language import FastRunAsyncFunction

from report.markdown_patterns import Form, write_file


class ReportsPlugin(Plugin, QObject):
    def __init__(self, bm):
        super().__init__(bm)
        self._client = Client(f"{os.path.dirname(os.path.dirname(__file__))}/markdown_api/"
                              f"api{'.exe' if sys.platform == 'win32' else ''}")
        self.fast_run_options = {'markdown': [
            FastRunAsyncFunction('Конвертировать в Docx', 'custom-docx', self.to_docx),
            FastRunAsyncFunction('Конвертировать в Pdf', 'custom-pdf', self.to_pdf)
        ]}
        self.files_create_options = {'md': (Form, lambda p, d: write_file(bm, p, d))}

    def terminate(self):
        self._client.terminate()

    async def to_docx(self, path, bm):
        resp = await self._client.post("convert/to-docx", {
            'src': path,
            'dst': path[:path.rindex('.')] + '.docx'
        })
        if not resp.ok:
            raise Exception(resp.data.get('message'))

    async def to_pdf(self, path, bm):
        resp = await self._client.post("convert/to-pdf", {
            'src': path,
            'dst': path[:path.rindex('.')] + '.pdf'
        })
        if not resp.ok:
            raise Exception(resp.data.get('message'))
