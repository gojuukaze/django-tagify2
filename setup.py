import sys

from setuptools import setup, find_packages

with open("README.rst", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-tagify2',
    version='1.0.4',
    description='django tag input field using tagify.js',
    url='https://github.com/gojuukaze/django-tagify2',
    author="gojuukaze",
    author_email="ikaze_email@163.com",

    long_description=long_description,
    license="GUN V3.0",
    packages=find_packages(exclude=['django_tagify*', 'example*', ]),

    install_requires=[
        'Django>=2.0.0',
    ],
    python_requires='>=3',
    platforms=['Any'],
    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Environment :: Web Environment',
    ],
)
