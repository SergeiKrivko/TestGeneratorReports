import os.path
import sys

from PyQt6.QtCore import QObject
from StdioBridge.client import Client
from TestGeneratorPluginLib import Plugin
from TestGeneratorPluginLib._language import FastRunAsyncFunction


class ReportsPlugin(Plugin, QObject):
    def __init__(self, bm):
        super().__init__(bm)
        self._client = Client(f"{os.path.dirname(os.path.dirname(__file__))}/markdown_api/"
                              f"api{'.exe' if sys.platform == 'win32' else ''}")
        self.fast_run_options = {'markdown': [
            FastRunAsyncFunction('Конвертировать в Docx', 'custom-docx', self.to_docx),
            FastRunAsyncFunction('Конвертировать в Pdf', 'custom-pdf', self.to_pdf)
        ]}

    async def to_docx(self, path, bm):
        resp = await self._client.post("convert/to-docx", {
            "path": path,
        })
        if not resp.ok:
            raise Exception(resp.data.get('message'))

    async def to_pdf(self, path, bm):
        resp = await self._client.post("convert/to-pdf", {
            "path": path,
        })
        if not resp.ok:
            raise Exception(resp.data.get('message'))
