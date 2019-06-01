#!/usr/bin/env python3

import sys

class PrexEngine:
	def __init__(self, source=None):
		self.source = sys.stdin if source == None else open(source, "r")
		print(self.source)

if __name__ == '__main__':
	# Parse command line options
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", action="store_true", default=False, help="show context")
	parser.add_argument("-i", action="store", dest="file", help="specify input file")
	parser.add_argument("INPUT", action="store", help="the regex pattern")
	args = parser.parse_args()
	# Construct PrexEngine
	prex = PrexEngine(args.file)
