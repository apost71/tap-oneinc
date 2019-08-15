#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-oneinc",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_oneinc"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-oneinc=tap_oneinc:main
    """,
    packages=["tap_oneinc"],
    package_data = {
        "schemas": ["tap_oneinc/schemas/*.json"]
    },
    include_package_data=True,
)
