#!/usr/bin/env python
from setuptools import setup

if __name__ == '__main__':
    setup(
        name='pyHIPIFY',
        version='0.0.0',
        description='Simple utility to transform CUDA source into HIP source',
        author='',
        package_data={
            'pyHIPIFY': ['*']
        },
        packages=[
            'pyHIPIFY',
        ],
        setup_requires=['setuptools']
    )
