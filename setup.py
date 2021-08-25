import os
from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='bgremover',
    packages=find_packages(include=['bgremover', 'bgremover.libs', 'bgremover.tools']),
    version='0.1.0',
    description='Background remove tool',
    author='Anodev (OPHoperHPO)[https://github.com/OPHoperHPO]',
    license='Apache License 2.0',
    install_requires=required,
    entry_points={
        "console_scripts": [
            "bgremover=bgremover.tools.main:cli",
            "bgremover_setup=bgremover.tools.setup:cli"
        ]
    }
)