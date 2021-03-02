# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['zoom.py'],
             pathex=['C:\\Users\\Lenovo\\PycharmProjects\\untitled'],
             binaries=[('./driver/chromedriver.exe', './driver')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas+=[('jsa.PNG','C:\\Users\\Lenovo\\PycharmProjects\\untitled','DATA'),('mpass.PNG','C:\\Users\\Lenovo\\PycharmProjects\\untitled','DATA'),('password.PNG','C:\\Users\\Lenovo\\PycharmProjects\\untitled','DATA')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='zoom',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
