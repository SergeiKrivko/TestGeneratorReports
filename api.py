from StdioBridge.api import BridgeAPI, errors

from backend.markdown_parser import convert

app = BridgeAPI()


@app.post('convert/to-docx')
def convert_to_docx(data: dict):
    print(f"Converting {data.get('src')} to {data.get('dst')}")
    if 'src' not in data or 'dst' not in data:
        raise errors.ErrorUnprocessableEntity
    convert(data['src'], data['dst'])


@app.post('convert/to-pdf')
def convert_to_docx(data: dict):
    print(f"Converting {data.get('src')} to {data.get('dst')}")
    if 'src' not in data or 'dst' not in data:
        raise errors.ErrorUnprocessableEntity
    convert(data['src'], data['dst'], pdf=True)


app.run()
