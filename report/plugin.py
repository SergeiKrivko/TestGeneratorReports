from TestGeneratorPluginLib import Plugin, FastRunFunction

from report import markdown_parser


class ReportsPlugin(Plugin):
    def __init__(self, bm):
        super().__init__(bm)
        self.fast_run_options = {'markdown': [
            FastRunFunction('Конвертировать в Docx', 'custom-docx',
                            lambda path, bm: (markdown_parser.convert(path, bm, pdf=False), '')),
            FastRunFunction('Конвертировать в Pdf', 'custom-pdf',
                            lambda path, bm: (markdown_parser.convert(path, bm, pdf=True), ''))
        ]}
