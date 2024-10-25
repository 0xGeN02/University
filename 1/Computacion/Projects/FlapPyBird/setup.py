import os
from distutils.core import setup
import sys as sys
import py2exe as py2

origIsSystemDLL = py2.build_exe.isSystemDLL
def isSystemDLL(pathname):
    dlls = ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll")
    if os.path.basename(pathname).lower() in dlls:
        return 0
    return origIsSystemDLL(pathname)
py2.build_exe.isSystemDLL = isSystemDLL

sys.argv.append('py2exe')

setup(
    name    =  'Flappy Bird',
    version =  '1.1',
    author  =  '0xGeN02, Original Version: Sourabath Verma',
    options =  {
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
        }
    },

    windows = [{
        'script': "flappy.py",
        'icon_resources': [
            (1, 'flappy.ico')
        ]
    }],

    zipfile=None,
)