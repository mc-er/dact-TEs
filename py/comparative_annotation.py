#!/usr/bin/env python


def parse_cls_file(filename, annotation):

    fin = open(filename)
    cl_reads_dict = {}
    count = 0
    max_cluster = max(list(annotation.keys()))

    while True:
        try:
            cluster_id = int(next(fin).rstrip().split()[0][3:])
            reads = next(fin).rstrip().split()

            for r in reads:
                cl_reads_dict[r] = {
                    "cluster": cluster_id,
                    "sequence": None,
                    "annotation": annotation[cluster_id]
                }

            count += 1

            if count == max_cluster:
                fin.close()
                break

        except StopIteration:
            fin.close()
            break

    return cl_reads_dict


def parse_fasta_file(filename, cl_reads_dict):

    fin = open(filename)

    while True:
        try:
            read_id = next(fin).rstrip()[1:]
            sequence = next(fin).rstrip()

            try:
                cl_reads_dict[read_id]["sequence"] = sequence
            except KeyError:
                continue

        except StopIteration:
            fin.close()
            break

    return cl_reads_dict


def parse_annotation_file(filename):

    fin = open(filename)
    annotation = {}

    for line in fin:
        line = line.rstrip().split()
        annotation[int(line[0])] = line[2]

    fin.close()

    return annotation


def main():
    import argparse as ap

    parser = ap.ArgumentParser()

    parser.add_argument(
        '-a', "--annotation", help="annotation in csv format (no header)",
        required=True, type=str
    )

    parser.add_argument(
        '-c', "--clsfile", help="cls file to parse",
        required=True, type=str
    )

    parser.add_argument(
        '-f', "--fasta", help="fasta file with reads",
        required=True, type=str
    )

    parser.add_argument(
        '-o', "--output", help="print read id and cluster information",
        required=True, type=str
    )

    args = parser.parse_args()

    annotation = parse_annotation_file(args.annotation)
    reads = parse_cls_file(args.clsfile, annotation)
    reads = parse_fasta_file(args.fasta, reads)
    output = open(args.output, "w")

    for key in reads.keys():
        read_id = key
        cluster = reads[key]["cluster"]
        sequence = reads[key]["sequence"]
        cltype = reads[key]["annotation"]
        out = "\t".join([str(cluster), read_id, cltype, sequence])
        # print(out, file=output)
        output.write(out + "\n")

    return 0


if __name__ == '__main__':
    main()
