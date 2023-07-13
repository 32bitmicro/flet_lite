from setuptools import setup, find_packages
import os

with open("README.md", encoding="utf-8") as f:
    long_descibe = str(f.read())

setup(
    name='flet_lite',
    version='1.7.5',
    author='SKbarbon',
    description='A tiny version of flet to work on mobile development',
    long_description=long_descibe,
    long_description_content_type='text/markdown',
    url='https://github.com/SKbarbon/flet_lite',
    install_requires=["flask_cors", "flask", "jsonpickle", "repath"],
    packages=find_packages(include=["flet", "flet_core", "flet.web", "flet/*", "flet.api"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
    include_package_data=True,
    include_dirs=["flet", "flet_core", "flet.web"]
)
