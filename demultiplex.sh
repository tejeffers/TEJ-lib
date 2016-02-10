####################################
#
# Tess Jeffers
# August 2012 
#!/bin/bash
# demultiplexing reads where index read is in a second file
# requires fastx toolkit installed globally
# run twice for paired end samples, replacing 
# read 1 with read 2 for the mate pair.
#
# syntax:
# demultiplex.sh read1.fastq indexRead.fastq barcodes.txt outputPrefix
####################################


paste -d '\0' <(echo; sed -n '1,${n;p;}' $1 | sed G) $2 | sed '/^$/d' | fastx_barcode_splitter.pl --bol --bcfile $3 --prefix $4
