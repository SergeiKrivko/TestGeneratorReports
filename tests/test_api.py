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

    resp = await client.post('convert/to-docx', {
        'src': 'test.md',
        'dst': 'results/test.docx',
    })
    if not resp.ok:
        raise Exception(resp.data)

    resp = await client.post('convert/to-pdf', {
        'src': 'test.md',
        'dst': 'results/test.pdf',
    })
    if not resp.ok:
        raise Exception(resp.data)


if __name__ == '__main__':
    asyncio.run(main())
