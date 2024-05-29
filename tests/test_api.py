import asyncio
import os
import sys

from StdioBridge.client import Client


async def main():
    path = f"{os.path.dirname(os.path.dirname(__file__))}/markdown_api/api"
    if sys.platform == 'win32':
        path += '.exe'
    client = Client(path)
    os.makedirs('results', exist_ok=True)
    print(os.getcwd())
    print(os.listdir('results'))

    resp = await client.post('convert/to-docx', {
        'src': os.path.join(os.path.dirname(__file__), 'test.md'),
        'dst': os.path.join(os.path.dirname(__file__), 'results/test.docx'),
    })
    if not resp.ok:
        raise Exception(resp.data)

    resp = await client.post('convert/to-pdf', {
        'src': os.path.join(os.path.dirname(__file__), 'test.md'),
        'dst': os.path.join(os.path.dirname(__file__), 'results/test.pdf'),
    })
    if not resp.ok:
        raise Exception(resp.data)


if __name__ == '__main__':
    asyncio.run(main())
