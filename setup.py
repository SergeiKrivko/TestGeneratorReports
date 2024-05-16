from TestGeneratorPluginLib import PluginSetup


plugin = PluginSetup(
    plugin='report.plugin.ReportsPlugin',
    name="Reports",
    description="## Официальное расширение\n\nПозволяет конвертировать файлы markdown в docx и pdf.\n",
    version="1.0.0",
    author="SergeiKrivko",

    directories=['report'],
    requirements=[
        'docx2pdf~=0.1.8', 'latex2mathml~=3.77.0', 'htmldocx~=0.0.6', 'pypdf~=3.17.4', 'python-docx~=1.1.0',
        'requests~=2.31.0'
    ],
)
