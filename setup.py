#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst',encoding='utf8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('requirements_dev.txt') as f:
    devrequirements = f.read().splitlines()

requirements = requirements

setup_requirements = [ ]

#test_requirements = devrequirements

setup(
    author="Mani Kumar",
    author_email='hi@manikumar.in',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="picToSquare (Pic To Square) is an experimental python script that 'squares up' every picture in a directory  to be Instagram ready.",
    entry_points={
        'console_scripts': [
            'pictosquare=pictosquare.pictosquare:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pictosquare',
    name='pictosquare',
    packages=find_packages(include=['pictosquare', 'pictosquare.*']),
    setup_requires=setup_requirements,
    #test_suite='tests',
    #tests_require=test_requirements,
    url='https://github.com/hithismani/pictosquare',
    version='0.1.0',
    zip_safe=False,
)
