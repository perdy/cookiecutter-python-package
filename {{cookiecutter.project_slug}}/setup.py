# -*- coding: utf-8 -*-

import os
import shutil
import sys

from pip.download import PipSession
from pip.req import parse_requirements as requirements
from setuptools import Command, setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] == 2:
    from codecs import open


def parse_requirements(f):
    return [str(r.req) for r in requirements(f, session=PipSession())]


class Dist(Command):
    description = 'Create dist packages'
    user_options = [
        ('clean', 'c', 'clean dist directories before build (default: false)')
    ]
    boolean_options = ['clean']

    def initialize_options(self):
        self.clean = False

    def finalize_options(self):
        pass

    def run(self):
        if self.clean:
            shutil.rmtree('build', ignore_errors=True)
            shutil.rmtree('dist', ignore_errors=True)
            shutil.rmtree('{{ cookiecutter.project_slug }}.egg-info', ignore_errors=True)

        self.run_command('sdist')
        self.run_command('bdist_wheel')


class Test(Command):
    description = 'Static code analysis and tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from runtests import main

        return main()


# Read requirements
_requirements_file = os.path.join(BASE_DIR, 'requirements.txt')
_tests_requirements_file = os.path.join(BASE_DIR, 'tests/requirements.txt')
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
        ] + _TESTS_REQUIRES
    },
    license='GPLv3',
    zip_safe=False,
    keywords=_KEYWORDS,
    classifiers=_CLASSIFIERS,
    test_suite='nose.collector',
    cmdclass={
        'test': Test,
        'dist': Dist,
    },
)
