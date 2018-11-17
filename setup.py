# -*-coding:utf-8-*-

from setuptools import setup, find_packages

setup(
    name="csv2arff",
    version="2.0",
    author=u"Uğur Soğukpınar",
    author_email="sogukpinar.ugur@gmail.com",
    url="https://github.com/ugursogukpinar/csv2arff",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "csv2arff = csv2arff.csv2arff:main",
        ],
    },
    license="LICENSE.txt",
    description="Csv to Arff converter",
    long_description=open("README.rst").read(),
    install_requires=list(filter(None, [
        "numpy",
    ])),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ]
)
