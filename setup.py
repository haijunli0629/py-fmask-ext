# This file is part of 'python-fmask_ext' - a cloud masking module
# Copyright (C) 2015  Neil Flood
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
from setuptools import find_packages

import fmask_ext
from numpy.distutils.core import setup, Extension

# use the latest numpy API
NUMPY_MACROS = ('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')

example = Extension(name='example',
                    define_macros=[NUMPY_MACROS],
                    extra_link_args=['-Xlinker', '-export-dynamic'],
                    extra_compile_args=['-Xlinker', '-export-dynamic'],
                    sources=['src/example.c'])
# This is for a normal build
fillminimaC = Extension(name='_fillminima',
                        define_macros=[NUMPY_MACROS],
                        extra_link_args=['-Xlinker', '-export-dynamic'],
                        extra_compile_args=['-Xlinker', '-export-dynamic'],
                        sources=['src/fillminima.c'])
valueIndexesC = Extension(name='_valueindexes',
                          define_macros=[NUMPY_MACROS],
                          extra_link_args=['-Xlinker', '-export-dynamic'],
                          extra_compile_args=['-Xlinker', '-export-dynamic'],
                          sources=['src/valueindexes.c'])
extensionsList = [example, fillminimaC, valueIndexesC]

# do the setup
setup(name='fmask_ext',
      version=fmask_ext.__version__,
      description='C-extension Module to implement the fmask cloud masking algorithm (Zhu, Wang & Woodcock 2015)',
      author='Neil Flood',
      author_email='neil.flood@des.qld.gov.au',
      packages=find_packages(),
      ext_package='fmask_ext',
      ext_modules=extensionsList,
      license='LICENSE.txt',
      data_files=[('', ['LICENSE.txt'])],  # add this to tarball
      url='https://www.pythonfmask.org/',
      classifiers=['Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'])
