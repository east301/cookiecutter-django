#!/usr/bin/env python3
#
#
#

import json
import os

from setuptools import find_packages, setup


# ================================================================================
# dependency
# ================================================================================

def get_dependencies(category):
    dependencies = []
    with open(os.path.join(os.path.dirname(__file__), 'Pipfile.lock')) as fin:
        for key, value in json.load(fin)[category].items():
            dependencies.append(key + value['version'])

    return dependencies


def find_package_data():
    result = {}
    for package in find_packages():
        data = []
        for key in ('static', 'templates'):
            for root, dirs, files in os.walk(os.path.join(package.replace('.', os.path.sep), key)):
                data.extend(os.path.join(root, n) for n in files)

        if data:
            result[package] = data

    return result


# ================================================================================
# setup
# ================================================================================

setup(
    name='{{cookiecutter.package_name}}',
    use_scm_version=True,
    license='TODO',

    description='{{cookiecutter.package_name}}',
    long_description='{{cookiecutter.package_name}}',
    url='TODO',

    author='TODO',
    author_email='TODO',

    keywords='TODO',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP'
    ],

    packages=find_packages(),
    include_package_data=True,

    install_requires=get_dependencies('default'),
    setup_requires=['setuptools_scm'],
    extras_require={
        'dev': get_dependencies('develop')
    },

    entry_points="""
        [console_scripts]
        {{cookiecutter.package_name}} = {{cookiecutter.package_name}}.cli:main
    """
)
