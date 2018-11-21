csv2arff
========

|PyPI Version| |Build Status|

.. |PyPI Version| image:: http://img.shields.io/pypi/v/csv2arff.svg
   :target: https://pypi.python.org/pypi/csv2arff
.. |Build Status| image:: https://travis-ci.org/ugursogukpinar/csv2arff.svg?branch=master
    :target: https://travis-ci.org/ugursogukpinar/csv2arff

Usage
-----

::

    $ csv2arff {input csv} {output arff}

see help for other options:

::

    $ csv2arff -h

    usage: csv2arff [-h] [-n NAME] [-d DELIMITER] [-v] input output

    positional arguments:
      input                 input CSV file name
      output                output ARFF file name

    optional arguments:
      -h, --help            show this help message and exit
      -n NAME, --name NAME  ARFF relation name
      -d DELIMITER, --delimiter DELIMITER
                            CSV delimiter
      -v, --verbose         verbose output
      -nl, --nolabel        first line without labels


Installation
------------

::

    $ [sudo] pip install csv2arff

Compatibility
-------------

Supported Python versions:

-  2.7
-  3.3
-  3.4
-  3.5

Tests
-----

::

    pip install -r requirements-dev.txt
    make test

Contributions
-------------

-  `@deric <https://github.com/deric>`_
-  `@KordianD <https://github.com/KordianD>`_
