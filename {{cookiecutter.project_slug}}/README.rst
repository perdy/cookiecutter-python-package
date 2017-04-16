*******************************
{{ cookiecutter.project_name }}
*******************************
|build-status| |coverage| |version|

:Version: {{ cookiecutter.version }}
:Status: Production/Stable
:Author: {{ cookiecutter.full_name }}

{{ cookiecutter.project_short_description }}.

Check full `{{ cookiecutter.project_name }} documentation`_.

.. _{{ cookiecutter.project_name }} documentation: http://{{ cookiecutter.project_slug }}.readthedocs.io
.. |build-status| image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?branch=master
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
.. |coverage| image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/badge.svg
    :alt: coverage
    :scale: 100%
    :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
.. |version| image:: https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg
    :alt: version
    :scale: 100%
    :target: https://badge.fury.io/py/{{ cookiecutter.project_slug }}
