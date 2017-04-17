# -*- coding: utf-8 -*-

import os
import sys

from pip.download import PipSession
from pip.req import parse_requirements as requirements
from setuptools import setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] == 2:
    from codecs import open


def parse_requirements(f):
    return [str(r.req) for r in requirements(f, session=PipSession())]


# Read requirements
_requirements_file = os.path.join(BASE_DIR, 'requirements.txt')
_tests_requirements_file = os.path.join(BASE_DIR, 'requirements-tests.txt')
_REQUIRES = parse_requirements(_requirements_file)
_TESTS_REQUIRES = parse_requirements(_tests_requirements_file)

# Read description
with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    _LONG_DESCRIPTION = f.read()

_CLASSIFIERS = (
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
{%- for version in cookiecutter.setup_info.python_versions %}
    'Programming Language :: Python :: {{ version }}',
{%- endfor %}
    'Topic :: Software Development :: Libraries :: Python Modules',
)

_KEYWORDS = ' '.join([
{%- for tag in cookiecutter.setup_info.package_tags %}
    '{{ tag }}',
{%- endfor %}
])

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}.',
    long_description=_LONG_DESCRIPTION,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    maintainer='{{ cookiecutter.full_name }}',
    maintainer_email='{{ cookiecutter.email }}',
    url='{{ cookiecutter.project_url }}',
    download_url='{{ cookiecutter.project_url }}',
    packages=[
        '{{ cookiecutter.app_slug }}',
    ],
    include_package_data=True,
    install_requires=_REQUIRES,
    tests_require=_TESTS_REQUIRES,
    extras_require={
        'dev': [
            'setuptools',
            'pip',
            'wheel',
            'twine',
            'bumpversion',
            'pre-commit',
        ] + _TESTS_REQUIRES,
    },
    license='GPLv3',
    zip_safe=False,
    keywords=_KEYWORDS,
    classifiers=_CLASSIFIERS,
)
