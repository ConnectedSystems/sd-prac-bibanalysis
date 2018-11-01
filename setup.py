#! /usr/bin/env python
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='Biblio',
        version='0.1.dev0',
        description='Python package collection to support bibliometric analysis',
        long_description=open('README.md').read(),
        url='',
        author='Takuya Iwanaga',
        author_email='iwanaga.takuya@anu.edu.au',
        license='(c) 2018 Takuya Iwanaga',
        packages=['wosis'],
        install_requires=[
            'lxml',
            'pyyaml',
            'wos',
            'metaknowledge',
            'matplotlib',
            'seaborn',
            'pandas',
            'networkx',
            'python-louvain',
            'nltk',
            'fuzzywuzzy',
            'python-levenshtein'
        ],
        dependency_links=[
            'pip install git+https://github.com/titipata/wos_parser.git',
            'pip install git+https://github.com/ConnectedSystems/wosis.git'
        ],
    )
