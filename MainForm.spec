# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Vistas\\MainForm.py'],
    pathex=['C:\\Users\\USER\\PycharmProjects\\CodificadorSerial'],  # Agrega la ruta de tu proyecto
    binaries=[],
    datas=[],
    hiddenimports=['Controladores.MainControl', 'Controladores.GraficadorControl',
                   'Modelos.Unipolar', 'Modelos.Graficador',
                   'Modelos.Polar.NRZL', 'Modelos.Polar.NRZI', 'Modelos.Polar.RZ',
                   'Modelos.Polar.Manchester', 'Modelos.Polar.ManchesterDiferencial',
                   'Modelos.Bipolar.AMI', 'Modelos.Bipolar.B8ZS', 'Modelos.Bipolar.HDB3',
                   'Vistas.GraficadorVista'],  # Agrega todos tus módulos
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
    name='CodificadorSerial',  # Cambia el nombre si quieres
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)