#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Futures

# Generic/Built-in
import argparse
import json

# Other Libs

#Module Info
__author__ = "Daniel Bielawa"
__copyright__ = "Copyright 2022, Daniel Bielawa"
__credits__ = ["Daniel Bielawa"]
__license__ = "MPL 2.0"
__version__ = "0.1.0"
__maintainer__ = "Daniel Bielawa"
__email__ = "dwbielawa@liberty.edu"
__status__ = "Dev"

# {code}
def toplevel(inputfile,outputfile):
	primarydatatree = {}
	with open(inputfile, newline='') as csvfile:
		for line in csvfile:
			line = line.replace("\r\n","")
			mysplit = line.split("\t")
			if mysplit[0] == "Description":
				continue
			else:
				filename = mysplit[1]
				primarydatatree[filename] = {}
				primarydatatree[filename]['filename'] = mysplit[1]
				primarydatatree[filename]['description'] = mysplit[0]
				primarydatatree[filename]['product'] = mysplit[2]
				primarydatatree[filename]['mainversion1'] = mysplit[3]
				primarydatatree[filename]['mainversion2'] = mysplit[4]
				primarydatatree[filename]['altversion'] = mysplit[5]
				primarydatatree[filename]['imglookup1'] = mysplit[6]
				primarydatatree[filename]['imglookup2'] = mysplit[7]
	data = json.dumps(primarydatatree)
	print(data, file=open(outputfile, 'a'))


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--inputfile', help='Input file from AKIPS API (api-ro) (mac2vspa)', required=True)
	parser.add_argument('-o','--outputfile', help='Output file reporting on ports with multiple MAC addresses.', required=True)

	args = parser.parse_args()
	inputfile = args.inputfile
	outputfile = args.outputfile
	toplevel(inputfile,outputfile)
