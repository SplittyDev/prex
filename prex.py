#!/usr/bin/env python3

import re
import sys
from itertools import tee
from typing import Sequence

class PrexEngine:
	def __init__(self, expr: str, source: str = None):
		self.eos = False
		self.expr = re.compile(expr)
		self.source = sys.stdin if source == None else open(source, "r")

	def readline(self) -> str:
		# Bail on EOS
		if self.eos:
			return None
		# Read line
		line = self.source.readline()
		# Test for EOS
		if line == '':
			self.eos = True
		return None if self.eos else line

	def __iter__(self):
		return self

	def __next__(self):
		lastmatch = None
		# Wait for valid match
		while lastmatch == None:
			# Read next line
			line = self.readline()
			# Stop iteration on EOS
			if line == None:
				raise StopIteration
			# Assign match
			lastmatch =  self.expr.match(line)
		# Return match groups
		return lastmatch.groups()

class Prex2Plain:
	def __init__(self, prex):
		self.prex = prex

	def run(self):
		for matches in self.prex:
			print(' | '.join(matches))

if __name__ == '__main__':
	# Define formatters
	fmts = {
		"plain": Prex2Plain,
	}
	# Parse command line options
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", action="store_true", default=False, help="show context")
	parser.add_argument("-i", action="store", dest="file", help="input file")
	parser.add_argument("-f", action="store", dest='format', help='output format')
	parser.add_argument("INPUT", action="store", help="regex pattern")
	args = parser.parse_args()
	# Determine formatter
	fmtc = fmts.get(args.format, Prex2Plain)
	# Construct PrexEngine
	prex = PrexEngine(args.INPUT, args.file)
	# Run formatter
	fmtc(prex).run()
