#!/usr/bin/env python
# -*-coding:utf-8-*-

import argparse
import numpy as np
import sys


class Csv2Arff():
    '''
      Reads a CSV file and determines attributes' types and converts
      to an ARFF file.
    '''

    def __init__(self, args):
        self.args = args
        self.attribute_types = {}
        if self.args.input == self.args.output:
            sys.exit("input file can't be the same as the output file!")
        self.read_csv()
        self.determine_attribute_types()
        self.write_arff()

    def read_csv(self):
        if self.verbose():
            print("Reading CSV file '%s'" % (self.args.input))
        data = np.genfromtxt(self.args.input, delimiter=self.args.delimiter,
                             dtype='str')
        self.columns = data[0]
        if self.is_without_labels():
            self.data = np.array(data[:])
        else:
            self.data = np.array(data[1:])

    def determine_attribute_types(self):
        if self.verbose():
            print('Calculating attribute types')
        for (i, attribute) in enumerate(self.columns):
            unique = list(set(self.data[:, i]))

            unique_value_index = 0
            while (unique_value_index < len(unique) and self.is_numeric(
                    str(unique[unique_value_index])) is not False):
                unique_value_index += 1

            self.attribute_types[attribute] = 'numeric'

            if (unique_value_index < len(unique)):
                unique.sort()
                unique = ["'%s'" % value for value in unique]
                self.attribute_types[
                    attribute] = '{' + ','.join(unique) + '}'

                column_data = np.copy(self.data[:, i])
                for (data_index, value) in enumerate(column_data):
                    column_data[data_index] = "'%s'" % str(value)

                self.data[:, i] = column_data
        if self.verbose():
            print('Found %i attributes' % (len(self.columns)))

    def write_arff(self):
        if self.verbose():
            print("Writing ARFF to '%s' file" % (self.args.output))

        new_file = open(self.args.output, 'w')

        # name from CLI arguments
        name = self.args.output
        if hasattr(self.args, 'name') and self.args.name is not None:
            name = self.args.name
        elif '.' in str(name):
            # name without extension
            pos = name.rfind('.')
            name = name[:pos]
        else:
            name = self.args.output

        # Write relation
        new_file.write('@relation ' + str(name) + '\n\n')

        self.write_attributes(new_file)

        # Prepare data
        lines = []
        for row in self.data:
            lines.append(','.join(row))

        # Write data
        new_file.write('@data\n')
        new_file.write('\n'.join(lines))
        new_file.close()

    def verbose(self):
        if hasattr(self.args, 'verbose') and self.args.verbose:
            return True
        else:
            return False

    def is_without_labels(self):
        return hasattr(self.args, 'nolabel') and self.args.nolabel

    def is_numeric(self, lit):
        'Return value of numeric literal string or ValueError exception'
        if not len(lit):
            return 0
        # Handle '0'
        if lit == '0':
            return 0
        # Hex/Binary
        litneg = lit[1:] if lit[0] == '-' else lit
        if litneg[0] == '0':
            if litneg[1] in 'xX':
                return int(lit, 16)
            elif litneg[1] in 'bB':
                return int(lit, 2)
            else:
                try:
                    return int(lit, 8)
                except ValueError:
                    pass

        # Int/Float/Complex
        try:
            return int(lit)
        except ValueError:
            pass
        try:
            return float(lit)
        except ValueError:
            pass

        return False

    def write_attributes(self, new_file):
        if self.is_without_labels():
            self._write_attributes_without_labels(new_file)
        else:
            self._write_attributes_with_labels(new_file)

    def _write_attributes_without_labels(self, new_file):
        for index, column in enumerate(self.columns):
            new_file.write(
                "@attribute col%i %s\n" %
                (index, self.attribute_types[column]))

    def _write_attributes_with_labels(self, new_file):
        for column in self.columns:
            new_file.write(
                "@attribute %s %s\n" %
                (column, self.attribute_types[column]))


def main():
    parser = argparse.ArgumentParser(prog='csv2arff')
    parser.add_argument('-n', '--name', help='ARFF relation name')
    parser.add_argument('-d', '--delimiter', help='CSV delimiter',
                        default=',')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="verbose output")
    parser.add_argument('-nl', '--nolabel', help='first line without labels',
                        action='store_true')
    parser.add_argument('input', help='input CSV file name')
    parser.add_argument('output', help='output ARFF file name')
    args = parser.parse_args()

    Csv2Arff(args)


if __name__ == '__main__':
    main()
