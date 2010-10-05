0.0.7 (June 2010)
  Cleaned up in order to create a Debian package.

0.0.6 (Mon, 14 Dec 2009)
  Debian packaging
  Removed from scripts files that were not scripts

0.0.5: (June 1st, 2009) From the Pygame project
  Output no longer calls abort when it deallocates.
  Added abort and close methods.
  Need to call Abort() explicityly if you want that to happen.

PyPortMidi v0.03 03/15/05
Python wrappings for PortMidi
John Harrison
harrison@media.mit.edu

PyPortMidi
----------

PyPortMidi is a Python wrapper for PortMidi. PortMidi is a cross-platform
C library for realtime MIDI control. Using PyPortMidi, you can send and
receive MIDI data in realtime from Python.

Besides using PyPortMidi to communicate to synthesizers and the
like, it is possible to use PyPortMidi as a way to send MIDI messages
between software packages on the same computer. 

PyPortMidi was written in Pyrex, a language for writing Python extension
modules.

Installing PyPortMidi from its Pyrex source code:
-------------------------------------------------

1. Linux only: install ALSA if it is not installed:
   http://www.alsa-project.org/

2. Install Pyrex if it is not installed
   http://nz.cosc.canterbury.ac.nz/~greg/python/Pyrex/

3. Choose to rebuild the PortMidi C library:
        a. download and extract PortMidi 
           http://www-2.cs.cmu.edu/~music/portmusic/

        b. Win32: - compile PortMidi with MS VC 6.0 (free download)
                  - use LIB from the MS VC 6.0 package to create
                    porttime.lib and portmidi.lib
                  - copy porttime.lib and portmidi.lib to
                    PyPortmidi's win32 subdirectory

        c. OS X:  - change to PortMidi subdirectory pm_mac
                  - compile. Type: xcodebuild -project pm_mac.pbproj
                  - copy newly created libportmidi.a to
                    PyPortMidi's OSX subdirectory

        d. Linux: - type <make> from PortMidi's root directory
                  - copy libportmidi.a
                         from portmidi's pm_linux directory
                         to PyPortMidi's linux directory
                  - copy libporttime.a
                         from portmidi's porttime directory
                         to PyPortMidi's linux directory

4. in PyPortMidi's root directory, type:
   python setup.py install
   (make sure you have admin/superuser privileges)

Distribution of PyPortMidi compiled code:
--------------------------------------------

I have provided a Win32 installer for Python 2.3.x. I would welcome
a Win32 installer for Python 2.4. I have *not* provided installers for
OS X or Linux because I suspect these users would rather compile
from source code. If this is not the case, please tell me.

Update: There is now a Debian package available from http://bitbucket.org/aalex/pyportmidi.

Using PyPortMidi
----------------
Running the test_pyportmidi.py sample script and looking at the code is the
easiest way to start. The classes and functions are mostly documented, or
seem self-explanatory. 

You can also look at the portmidi.h header, which heavily documents all
of PortMidi's functions.

Bugs, suggestions etc.
----------------------
I welcome any bugs you have to report or any suggestions you have about
how to improve the code and the interface.

-John

