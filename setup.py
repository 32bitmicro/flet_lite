from setuptools import setup, find_packages
import os

with open("README.md", encoding="utf-8") as f:
    long_descibe = str(f.read())

setup(
    name='flet_lite',
    version='1.0',
    author='SKbarbon',
    description='A tiny version of flet to work on mobile developments',
    long_description=long_descibe,
    long_description_content_type='text/markdown',
    url='https://github.com/SKbarbon/flet_lite',
    install_requires=["flet_core", "flask_cors", "flask", "requests"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
    include_package_data=True,
    include_dirs=["web"]
)
