#!/usr/bin/env python
#-*-mode:python-*-
#
# distutils setup script for ttb
# Time-stamp: <2008-11-29 13:53:48 (djcb)>
#

import sys
import glob
import os.path

try:
    from distutils.core import setup
except:
    sys.exit ("""
    TTB Installation Failed
    -----------------------
    Could not import the Python distutils package. Please install the package.
    The package is probably called:
    - 'python2.x-setuptools' (2.x for your python version) [Debian, Ubuntu,...]
    - 'python-dev'  [Debian/Etch]
    - 'python-devel' [Novell/Suse]
    - 'python2-devel' [RedHat]
    - 'libpython2.4-devel' [Mandriva] (version may be different)
    """)

name = 'ttb'
version = '0.9.5'
long_desc = '''
TTB Teletekst Browser is a small browser for the Teletekst system
as used in The Netherlands, and provides a convenient way to stay
up to date with news, sports, weather, stock exchange and what not'''


#
# distutils dance
#
datadir = 'share/ttb/'


# do the setup
try: 
    setup(name             = name,
          version          = version,
          description      = 'TTB Teletekst Browser',
          long_description = long_desc,
          author           = 'Dirk-Jan C. Binnema',
          author_email     = 'djcb@djcbsoftware.nl',
          url              = 'http://www.djcbsoftware.nl/code/ttb',
          license          = 'GPL',
          scripts          = ['src/ttb'],
          data_files       = [("share/applications", ['ttb.desktop']),
                              ("share/pixmaps",      ["images/ttb.png"]),
                              (datadir,              ["glade/ttb.glade"])])
except:
    (t,msg,x) = sys.exc_info()

    msg = msg.__str__()
    if msg.find("Makefile") != -1:  # ooh brutal hack

        sys.exit ("""
        TTB Installation Failed
        -----------------------
        It seems your Python installation is missing the 'dev'-package.
        Please install it.
        
        The package is probably called:
        - 'python2.x-setuptools' (2.x for your python version) [Debian, Ubuntu,...]
        - 'python-dev'  [Debian/Etch]
        - 'python-devel' [Novell/Suse]
        - 'python2-devel' [RedHat]
        - 'libpython2.4-devel' [Mandriva] (version may be different)
        """)

    else:
        sys.exit ("""
        TTB Installation Failed
        -----------------------
        Something went wrong:

        """
        + msg +
        """

        If you cannot figure out the solution yourself, please report the problem
        to djcb@djcbsoftware.nl.
        """)
