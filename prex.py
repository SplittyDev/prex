#!/usr/bin/env python3

import re
import sys
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

	def match(self, line: str) -> Sequence[str]:
		matches = self.expr.match(line)
		print(matches)
		pass

	def __iter__(self):
		return self

	def __next__(self) -> str:
		line = self.readline()
		if line == None:
			raise StopIteration
		return line

if __name__ == '__main__':
	# Parse command line options
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", action="store_true", default=False, help="show context")
	parser.add_argument("-i", action="store", dest="file", help="specify input file")
	parser.add_argument("INPUT", action="store", help="the regex pattern")
	args = parser.parse_args()
	# Construct PrexEngine
	prex = PrexEngine(args.INPUT, args.file)
	for line in prex:
		groups = prex.match(line)
