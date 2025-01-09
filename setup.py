from cx_Freeze import setup, Executable

# cx_Freeze 使用
# 配置好 setup.py 文件后，
# 你就可以使用以下命令来打包你的应用了：
# python setup.py build
# 如果你想创建一个安装程序，可以使用：
# python setup.py bdist_msi

build_options = {'packages': [],
                 "bin_excludes": ['Qt6Qml.dll', 'Qt6Network.dll', 'Qt6Pdf.dll', 'QtNetwork.pyd',
                                  'Qt6QmlMeta.dll', 'Qt6QmlModels.dll', 'Qt6QmlWorkerScript.dll',
                                  'Qt6Quick.dll', 'Qt6VirtualKeyboard.dll', 'Qt6Svg.dll'
                                  ],
                 'excludes': [],
                 'include_files': ['./settings.json']
                 }

base = 'gui'

executables = [
    Executable('painterControl.py', base=base)
]

setup(name='PainterControl',
      version='1.0',
      description='',
      options={'build_exe': build_options},
      executables=executables)
