from TestGeneratorPluginLib import PluginSetup


plugin = PluginSetup(
    plugin='report.plugin.ReportsPlugin',
    name="Reports",
    description="## Официальное расширение\n\nПозволяет конвертировать файлы markdown в docx и pdf.\n",
    version="1.1.2",
    url="https://github.com/SergeiKrivko/TestGeneratorReports",
    author="SergeiKrivko",

    directories=['report', 'markdown_api'],
    platform_specific=True,
)
