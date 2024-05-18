from TestGeneratorPluginLib import PluginSetup


plugin = PluginSetup(
    plugin='report.plugin.ReportsPlugin',
    name="Reports",
    description="## Официальное расширение\n\nПозволяет конвертировать файлы markdown в docx и pdf.\n",
    version="1.1.1",
    author="SergeiKrivko",

    directories=['report', 'markdown_api'],
)
