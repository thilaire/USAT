""""This file is part of USAT.

	MIT License

	Copyright (c) 2022 - Thibault Hilaire

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.


USAT is a simple tool that taks survey from Usabilla and plot attrakdiff plots.
It is written by Thibault Hilaire

File: setup.py
Date: Feb 2022

	setup.py file to install USAT
"""


from setuptools import setup


def readme():
    """include the readme"""
    with open('README.md') as f:
        return f.read()


setup(name='USAT',
      version='0.1',
      description='A simple tool that taks survey from Usabilla and plot attrakdiff plots',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Education',
        'Intended Audience :: Science/Research'
      ],
      keywords='Usabilla attrakdiff',
      url='https://github.com/thilaire/USAT',
      author='Thibault Hilaire',
      author_email='thibault@docmatic.fr',
      license='MIT',
      install_requires=['matplotlib', 'pandas', 'streamlit'],
      entry_points={'console_scripts': ['USAT=src.USAT']},
      include_package_data=True,
      zip_safe=False
)