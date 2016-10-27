#! /usr/bin/python
#License MIT 2016 Ahmad Retha

import sys
import gzip

help = "Correct usage example: python extractChromosome.py hs37d5.fa.gz 21 chr21.fa\n\
The required first argument is the large gzipped fasta file (can be uncompress fasta too) with all the chromosomes in it.\n\
The required second argument is the chromosome number to extract (1..22, X, Y).\n\
The optional third argument is the file to write it out to."

argc = len(sys.argv)

if argc == 1 or (argc == 2 and sys.argv[1].startswith('-h')):
    print help
    sys.exit(0)

if not (argc == 3 or argc == 4):
    print 'Invalid number of arguments!'
    print help
    sys.exit(1)

inFile = None

try:
    if sys.argv[1].endswith('.gz'):
        inFile = gzip.open(sys.argv[1], 'rb')
    else:
        inFile = open(sys.argv[1], 'r')
except IOError:
    print 'Invalid file or unable to open file for reading ', sys.argv[1]
    print help
    sys.exit(1)

chrNo = 0

try:
    if sys.argv[2] == 'X' or sys.argv[2] == 'Y':
        chrNo = sys.argv[2]
    else:
        chrNo = str(int(sys.argv[2]))
except ValueError:
    print 'Invalid chromosome number! ', sys.argv[2]
    print help
    sys.exit(1)

outFile = None

if argc == 4:
    try:
        outFile = open(sys.argv[3], 'w');
    except IOError:
        print 'Invalid file or unable to open file for writing ', sys.argv[3]
        print help
        sys.exit(1)

copy = False
for line in inFile:
    if line == '':
        continue
    if copy:
        if line.startswith('>'):
            break
        else:
            if outFile:
                outFile.write(line)
            else:
                print line,
    elif line.startswith('>' + chrNo):
        copy = True
        if outFile:
            outFile.write(line)
        else:
            print line,

inFile.close()
if outFile:
    outFile.close()

