#!-*-coding:utf-8 -*-
#!/usr/bin/env

import numpy as np
import sys

class Csv2Arff:
	'''
		It reads csv files and determines type of attributes and saves as arff file.
	'''
	def __init__(self, input_csv, output_arff):
		self.input_csv = input_csv
		self.output_arff = output_arff
		self.attribute_types = {}
		self.read_csv()
		self.determine_attribute_types()
		self.write_arff()

	def read_csv(self):
		print "\nReading csv file to convert arff file\n"
		data = np.genfromtxt(self.input_csv, delimiter=',', dtype=None)
		self.columns = data[0]
		self.data = np.array(data[1:])

	def determine_attribute_types(self):
		print "\nCalculating attribute types\n"
		for (i, attribute) in enumerate(self.columns):
			unique_values = list(set(self.data[:,i]))

			unique_value_index = 0
			while (unique_value_index < len(unique_values) and self.is_numeric(str(unique_values[unique_value_index])) is not False):
				unique_value_index += 1

			self.attribute_types[attribute] = 'numeric'

			if (unique_value_index < len(unique_values)):
				unique_values = ["'%s'" % str(value) for value in unique_values]
				self.attribute_types[attribute] = '{' + ','.join(unique_values) + '}'

				column_data = np.copy(self.data[:,i])
				for (data_index, value) in enumerate(column_data):
					column_data[data_index] = "'%s'" % str(value)

				self.data[:,i] = column_data



	def write_arff(self):
		print "\nWriting as arff file\n"
		new_file = open(self.output_arff, 'w')

		# Write relation
		new_file.write('@relation ' + str(self.output_arff)+ '\n\n')

		# Write attributes
		for column in self.columns:
			new_file.write("@attribute %s %s\n" % (column, self.attribute_types[column]))

		# Prepare data
		lines = []
		for row in self.data:
			lines.append(','.join(row))

		#Write data
		new_file.write('@data\n')
		new_file.write('\n'.join(lines))
		new_file.close()

	def is_numeric(self, lit):
	    'Return value of numeric literal string or ValueError exception'
	    if not len(lit): return 0
	    # Handle '0'
	    if lit == '0': return 0
	    # Hex/Binary
	    litneg = lit[1:] if lit[0] == '-' else lit
	    if litneg[0] == '0':
	        if litneg[1] in 'xX':
	            return int(lit,16)
	        elif litneg[1] in 'bB':
	            return int(lit,2)
	        else:
	            try:
	                return int(lit,8)
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

def main():
	Csv2Arff(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()

