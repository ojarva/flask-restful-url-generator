"""
Packaging for flask-restful-url-generator
"""

from os import path
from codecs import open as codecs_open
from setuptools import setup

CURRENT_PATH = path.abspath(path.dirname(__file__))

with codecs_open(path.join(CURRENT_PATH, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='flask_restful_url_generator',
    version='0.0.1',
    description='flask-restful URLs list',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/ojarva/flask-restful-url-generator',
    author='Olli Jarva',
    author_email='olli@jarva.fi',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='flask restful',
    packages=["flask_restful_url_generator"],
    install_requires=['flask_restful'],
    extras_require={
        'dev': ['twine', 'wheel'],
    },
)
