#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='ipynb2viewer',
    version='0.2.1',
    description='Post IPython notebook files to nbviewer. IPython notebook content will be posted to gist.github.com.',
    long_description=readme + '\n\n' + history,
    author='kracekumar',
    author_email='me@kracekumar.com',
    url='https://github.com/kracekumar/ipynb2viewer',
    packages=[
        'ipynb2viewer',
    ],
    package_dir={'ipynb2viewer': 'ipynb2viewer'},
    include_package_data=True,
    install_requires=['requests==2.0.1', 'docopt==0.6.1', 'simplejson'
    ],
    license="BSD",
    zip_safe=False,
    keywords='ipynb2viewer, ipython',
    entry_points={
        'console_scripts': [
            'ipynb2viewer = ipynb2viewer.ipynb2viewer:main',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
