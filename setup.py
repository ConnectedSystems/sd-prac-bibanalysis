#! /usr/bin/env python
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='Biblio',
        version='0.1.1',
        description='Repository holding analysis process used to collect data and figures for a paper on \
                     software best practices in Integrated Environmental Modeling',
        long_description=open('README.md').read(),
        url='',
        author='Takuya Iwanaga',
        author_email='iwanaga.takuya@anu.edu.au',
        license='(c) 2018 Takuya Iwanaga',
        dependency_links=[
            'pip install git+https://github.com/ConnectedSystems/wosis.git'
        ],
    )
