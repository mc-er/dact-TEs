###############################################
##### to run py/comparative_annotation.py #####
###############################################
usage: comparative_annotation.py [-h] -a ANNOTATION -c CLSFILE -f FASTA -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -a ANNOTATION, --annotation ANNOTATION
                        annotation in csv format (no header)
  -c CLSFILE, --clsfile CLSFILE
                        cls file to parse
  -f FASTA, --fasta FASTA
                        fasta file with reads
  -o OUTPUT, --output OUTPUT
                        print read id and cluster information

file examples:

-a annotation.csv
head file.csv
1  58034	annotation-1
2	 19942	annotation-2
3	 19540	annotation-3
4	 16117	annotation-2
5	 15678	annotation-4
6	 15218	annotation-4
7	 14455	annotation-4
8	 13458	annotation-2
9	 12187	annotation-2
10	11776	annotation-5

-c hitsort.cls found in the Repeat Explorer output. [output-archive/seqclust/clustering/hitsort.cls]

-f reads.fasta found in the Repeat Explorer output. [output-archive/seqclust/reads/reads.fasta]

-o output-file.txt
head output-file.txt
7	readID_113842f	annotation-4	AGATCTACAACTTTGATGTTGAACACTTATCCTAAAAATGTCATATAGGGCGTCTATTTTCAAAGGGCGCGTGTTCTGCGTATATTACCTAAACTATGCGACTCGCAATTGTTCTGCGCGGTGTC
4	readID_224959f	annotation-2	AAATGCGATATAGGAGGTCTATTTTCAAAAGGCGCGACACCGCGCAGAACAATTGCGAGTCGCATAGTTTAGGTAATATACGCAGAACACGCGCCCTTTGAAAATAGACACCCTATATGACATTT
5	readID_224959r	annotation-4	ATCGCATTTTTAGGAAAAGTGTTCAACATCAAAGTTGTAGATCTCGTCGAGATCTACAACTTTGATGTTGAACACTTTCCCTAAAAATGTCATATAGGGCGTCTATTTTCAAAGGGCGCGTGTTC
1	readID_225027f	annotation-1	TCCTAAAAATGCGATATAGGAGGTCTATTTTCAAAAGGCGCGACATCACGCAGAACAATTGCGAGTCGCATAGTTTAGGTAATATACGCAGAACACGCGCCCTTTGAAAATAGACGCCCTATATG
4	readID_225804f	annotation-2	CTTTTCCTAAAAATGTCATATAGGGCGTCTATTTTCAAAGGGCGCGTGTTCTGCGTATATTACCTAAACTATGCGACTCGCAATTGTTCTGCGCGGTGTCGCGCCTTTTGAAAATAGACCTCCTA
8	readID_225804r	annotation-2	AAAAGTGTTCAACATCAAAGTTGTAGATCTCGACGAGATCTACAACTTTGATGTTGAACACTTTTCCTAAAAATGCGATATAGGAGGTCTATTTTCAAAAGGCGCGACACCGCGCAGAACAATTG
1	readID_225910f	annotation-1	GGAACAATTGCGAGTCGCATAGTTTAGGTAATATACACAGAACACGCGCCCTTTGAAAATAGACGCCATATATGACATATTTAGGAAAAGTGGTCAACATCAAAGTTGTAGATCTCGACGAGATC
1	readID_225910r	annotation-1	AACATCAAAGTTGTAGATCTCGTCGAGATCTACAACTTTGATGTTGAACACTTTTCCTAAAAATGTCATATATCGAGTCTATTTTCAAAGGGCGCGTGTTCTGCGTATATTACCTAAACTATGCG
4	readID_226262r	annotation-2	TCAGAACACGCGCCCTTTGAAAATAGACGCCATATATGACATTTTTAGGAAAAGTGTTCAACATCAAAGTTGTAGATCTCGACGAGATCTACAACTTTGATGTTGAACACTTTTCTTAAAAATGC
5	readID_227755f	annotation-4	AACTTTGATGTTGAACAGTTTTCCTAAAAATGTCATATAGGGCGTCTATTTTCAAAGGGCGCGTGTTCTGCGTATATTACCTAAACTATGCGACTCGCAATTGTTCTGCGCGGTGTCGCGCCTTT



###############################################
########## to run py/annotateCOMP.py ##########
###############################################
usage: annotateCOMP.py [-h] -c COMPCLS -d ANNOTFILES [ANNOTFILES ...] -m MAXCLUSTER [-o [OUTFILE]]

optional arguments:
  -h, --help            show this help message and exit
  -c COMPCLS, --compCLS COMPCLS
                        comparative analysis .cls file
  -d ANNOTFILES [ANNOTFILES ...], --annotFiles ANNOTFILES [ANNOTFILES ...]
                        Directory of read annotation files
  -m MAXCLUSTER, --maxCluster MAXCLUSTER
                        maximum cluster to check in comparative [INT]
  -o [OUTFILE], --outFILE [OUTFILE]
                        output file, default STDOUT

file examples:

-c hitsort.cls found in the Repeat Explorer output, comparative analysis. [output-archive/seqclust/clustering/hitsort.cls]

-d files produced by py/comparative_annotation.py.

-m INT, usually the last cluster to be annotated.

-o comp-annotation-summary.txt
head comp-annotation-summary.txt
CL1	 annotation-1: 0.9996,unclassified: 0.0004
CL2	 annotation-4: 0.9893,unclassified: 0.0104,annotation-1: 0.0003
CL3	 annotation-1: 0.994,unclassified: 0.006
CL4	 annotation-9: 0.9798,unclassified: 0.0181,annotation-7 0.0021
CL5	 annotation-2: 0.9459,unclassified: 0.0542,
CL6	 annotation-2: 1.0
CL7	 annotation-5: 0.9669,unclassified: 0.0293,6: 0.0021,annotation-3: 0.0017
CL8	 annotation-2: 0.9783,unclassified: 0.0217
CL9	 annotation-2: 0.9952,unclassified: 0.0048
CL10	annotation-2: 0.9919,unclassified: 0.008,annotation-1: 0.0001
