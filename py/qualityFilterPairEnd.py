#!/usr/bin/env python

def arguments():
	import argparse, sys
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--forwardFILE", help = "Forward read file, fastq format", type=argparse.FileType('r'), required=True)
	parser.add_argument("-r", "--reverseFILE", help = "Forward read file, fastq format", type=argparse.FileType('r'), required=True)
	parser.add_argument("-of", "--outFORWARD", help = "Output fastq file", type=argparse.FileType('w'), required=True)
	parser.add_argument("-or", "--outREVERSE", help = "Output fastq file", type=argparse.FileType('w'), required=True)
	parser.add_argument('-q', '--minq',help="min qual thresh for counting nucleotide as good enough, [INT]", required=False, type=int, default=20)
	parser.add_argument('-b', '--basep',help="percent bases per seq required to be above minq thresh, [FLOAT]",required=False, type=float, default=0.95)
	parser.add_argument('-n', '--ns',help="number of N allowed in each seq",required=False, type=int, default=0)
	ArgP = parser.parse_args()
	return ArgP

def next_n_lines(file_opened, N):
	from itertools import islice
	return [x.strip() for x in islice(file_opened, N)]


def check_qual(bases, quals, minq, basep, ns):

    Ns = bases.count("N")
    good_bases = sum([1 if ord(x)-33 >= minq else 0 for x in quals])

    return (Ns <= ns) and (good_bases/len(bases) >= basep)

def main():
	import re

	args = arguments()

	MQ = args.minq
	BP = args.basep
	NN = args.ns

	with args.forwardFILE as forF, args.reverseFILE as revF:
		forLines = next_n_lines(forF, 4)
		revLines = next_n_lines(revF, 4)

		while (forLines != []) and (revLines != []):

			good_fwd = check_qual(forLines[1], forLines[3], minq=MQ, basep=BP, ns=NN)
			good_rev = check_qual(revLines[1], revLines[3], minq=MQ, basep=BP, ns=NN)

			if good_fwd and good_rev:
				for fL in forLines:
					args.outFORWARD.write(fL + "\n")
				for rL in revLines:
					args.outREVERSE.write(rL + "\n")

			forLines = next_n_lines(forF, 4)
			revLines = next_n_lines(revF, 4)

main()
