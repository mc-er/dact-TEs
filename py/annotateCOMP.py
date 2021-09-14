#!/usr/bin/env python

def arguments():
    import argparse, sys
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', "--compCLS", help="comparative analysis .cls file", type=argparse.FileType('r'), required=True)
    parser.add_argument("-d", "--annotFiles", help = "Directory of read annotation files", type=str, required=True, nargs='+')
    parser.add_argument('-m', "--maxCluster", help="maximum cluster to check in comparative", type=int, required=True)
    parser.add_argument("-o", "--outFILE", help="output file, default STDOUT", nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    ArgP = parser.parse_args()
    return ArgP

def readAnnotFile(fileName, D):
    f = open(fileName)
    for line in f:
        line = line.strip().split()
        D[line[1]] = line[2]
    return D

def next_n_lines(file_opened, N):
	from itertools import islice
	return [x.strip() for x in islice(file_opened, N)]

def filterAnnotation(ANNOTATION, noREADS):
    import operator

    outDICT = {}
    for key in ANNOTATION.keys():
        if ANNOTATION[key] > 0:
            outDICT[key] = round(float(ANNOTATION[key]/noREADS),4)
    return(dict(sorted(outDICT.items(), key=operator.itemgetter(1),reverse=True)))


def countReadAnnot(READS, RAD):
    annotation = {}

    for read in READS:
        if read in RAD.keys():
            annot = RAD[read]
            if not annot in annotation:
                annotation[annot] = 1
            else:
                annotation[annot] += 1

    annotFILTsorted = filterAnnotation(annotation, len(READS))

    out = ""
    for aFS in annotFILTsorted:
        out = out + aFS + ": " + str(annotFILTsorted[aFS]) + ","

    return out.strip(",")

def main():
    import os

    args = arguments()
    maxCLUSTER = "CL" + str(args.maxCluster)

    print("Making annotation dict...")
    annotDICT = {}
    for annFile in args.annotFiles:
        annotDICT = readAnnotFile(annFile, annotDICT)

    print("Summerise annotation per cluster...")
    with args.compCLS as ccf:
        lines = next_n_lines(ccf, 2)

        while lines != []:
            cluster = lines[0].strip().split("\t")[0].strip(">")
            reads = lines[1].strip().split("\t")

            clusterANNOT = countReadAnnot(reads, annotDICT)

            args.outFILE.write("\t".join([cluster, clusterANNOT]) + "\n")

            if cluster == maxCLUSTER:
                break
            else:
                lines = next_n_lines(ccf, 2)


main()
