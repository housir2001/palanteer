# The MIT License (MIT)
#
# Copyright(c) 2021, Damien Feneyrou <dfeneyrou@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions :
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys
from setuptools import setup, find_packages, Extension

# Constants
isDevMode = False  # Enable to speed up development cycles. Shall be False for final installation


# Deduce some parameters
extra_link_args         = []
extra_compilation_flags = ["-I", os.path.normpath("../c++")]

if isDevMode:
    if sys.platform=="win32":
        extra_compilation_flags.append("/Zi")
        extra_link_args.append('/DEBUG')
    else:
        extra_compilation_flags.append("-O0")  # Debug symbols are already generated

classifiers_list = [
    'Intended Audience :: Developers',
    "Intended Audience :: Science/Research",
    'License :: OSI Approved :: MIT License',
    'Development Status :: 4 - Beta',
    "Programming Language :: Python :: 3",
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: Implementation :: CPython',
    'Environment :: Console',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: POSIX :: Linux',
    'Topic :: Software Development',
    'Topic :: Software Development :: Debuggers'
]


# Build call
setup(name="palanteer",
      version="0.1.0",
      author="Damien Feneyrou",
      author_email="dfeneyrou@gmail.com",
      license="MIT",
      description="Palanteer instrumentation library for Python language",
      classifiers=classifiers_list,
      python_requires=">=3.7",
      #url="",
      packages=find_packages(),
      ext_modules=[
          Extension('palanteer._cextension',
                    sources=[os.path.normpath('palanteer/_cextension/pyPalanteerInstrumentation.cpp')],
                    extra_compile_args=extra_compilation_flags,
                    extra_link_args   =extra_link_args)
      ],
      zip_safe=False
      )
