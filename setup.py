#!/usr/bin/env python
from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext
import sys

name = "pyPortMidi"
description="Python Wrappings for PortMidi",
version="0.0.7"
url = 'http://bitbucket.org/aalex/pyportmidi' #'http://sound.media.mit.edu/~harrison/pyportmidi/',
long_description = """pyPortMidi: Supports streaming realtime MIDI from Python using the cross-platform PortMidi C library"""
author = 'John Harrison'
author_email = 'harrison@media.mit.edu'
cmdclass = {'build_ext': build_ext}
scripts = [] #'test.py','README.txt'

if sys.platform == 'win32':
    print("Found Win32 platform")
    setup(
        name = name,
        description=description,
        version=version,
        url = url,
        long_description = long_description,
        author = author,
        author_email = author_email,
        cmdclass = cmdclass,
        scripts = scripts,
        ext_modules=[ 
            Extension(
                "pypm", ["pypm.pyx"],
                library_dirs = ["./win32"],
                libraries = ["portmidi", "winmm", "porttime"]
                )
        ]
)
elif sys.platform == 'darwin':
    print("Found darwin (OS X) platform")
    setup(
        name = name,
        description=description,
        version=version,
        url = url,
        long_description = long_description,
        author = author,
        author_email = author_email,
        cmdclass = cmdclass,
        scripts = scripts,
        ext_modules=[ 
            Extension(
                "pypm", ["pypm.pyx"],
                library_dirs=["./OSX"],
                libraries = ["portmidi"],
                extra_link_args=[
                    "-framework", "CoreFoundation",
                    "-framework", "CoreMIDI",
                    "-framework", "CoreAudio"]
                )
        ]
    )
else:
    print("Assuming Linux platform")
    setup(
        name = name,
        description=description,
        version=version,
        url = url,
        long_description = long_description,
        author = author,
        author_email = author_email,
        cmdclass = cmdclass,
        scripts = scripts,
        ext_modules=[ 
            Extension(
                "pypm", ["pypm.pyx"],
                library_dirs=["./linux"],
                libraries = ["portmidi", "porttime", "asound", "pthread"]
                )
        ]
    )
