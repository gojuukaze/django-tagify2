# -*- coding: utf-8 -*-
import sys

from setuptools import setup

import ktag

setup(
    name='django-ktag',
    version='0.0.1',
    description='django tag input field ',
    url='https://github.com/gojuukaze/django-ktag',
    author="gojuukaze",
    author_email="i@ikaze.uu.me",

    long_description=open("README.rst").read(),
    license="GUN V3.0",
    packages=[
        'ktag',
    ],
    install_requires=[
        'Django>=2.0.0',
    ],
    platforms=['Any'],
    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
    ],
)
