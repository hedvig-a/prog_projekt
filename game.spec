# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['game.py'],
    pathex=[],
    binaries=[],
    datas=[('background.jpg', '.'), ('background2.jpg', '.'), ('bamboosegment.png', '.'), ('bambooshoot.png', '.'), ('button.py', '.'), ('button_quit.png', '.'), ('button_resume.png', '.'), ('HOME.mp3', '.'), ('kivi.png', '.'), ('kork.png', '.'), ('kott.png', '.'), ('player.png', '.'), ('player_shift.png', '.'), ('straw.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)