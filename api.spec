# -*- mode: python ; coding: utf-8 -*-

import os


lib_path = ''
for root, _, _ in os.walk('venv'):
    if root.endswith('site-packages'):
        lib_path = root
        break


a = Analysis(
    ['api.py'],
    pathex=[],
    binaries=[],
    datas=[('backend/MML2OMML.XSL', 'backend'),
           (f'{lib_path}/latex2mathml/unimathsymbols.txt', 'latex2mathml')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='api',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='markdown_api',
)
