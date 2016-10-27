## Extract Chromosome

This is a small Python script that allows you to extract individual chromosomes from a large gzipped or uncompressed fasta file.

The 1000 genomes project stores the whole reference genome (GRCh37) in a large gzipped file nearly 900MB in size. Uncompressed this is 3.2GB.
You can use this utility to obtain individual chromosomes from that file without needing to extract it, like so:

`python extractChromosome.py hs37d5.fa.gz 21 chr21.fa`

The required first argument is the large gzipped fasta file (can be uncompress fasta too) with all the chromosomes in it.
The required second argument is the chromosome number to extract (1..22, X, Y).
The optional third argument is the file to write it out to.

License MIT 2016 Ahmad Retha
