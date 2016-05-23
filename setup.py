#-*-coding:utf-8-*-
import sys
from setuptools import *

setup(
    name="csv2arff",
    version="1.0",
    author="Uğur Soğukpınar",
    author_email="sogukpinar.ugur@gmail.com",
    url="https://github.com/ugursogukpinar/csv2arff",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "csv2arff = scripts.csv2arff:main",
        ],
    },
    license="LICENSE.txt",
    description="Csv to Arff converter",
    long_description=open("README.txt").read(),
    install_requires=list(filter(None, [
        "numpy",
    ])),
)