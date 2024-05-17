from StdioBridge.api import Api

from backend.markdown_parser import convert

app = Api()


@app.post('convert/to-docx')
def convert_to_docx(data: dict):
    convert(data['path'], pdf=False)


@app.post('convert/to-pdf')
def convert_to_docx(data: dict):
    convert(data['path'], pdf=True)


app.run()
