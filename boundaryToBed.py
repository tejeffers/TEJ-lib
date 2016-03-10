#############################################################################
#
# Tess Jeffers
# April 2012
#
# Goal: given a list of boundary nucleosomes from JGT, 
# create a .bed file that ranges from 
# 5' boundary - upstream offset to 3' boundary + downstream offset
#
# 
# Java Genomics Toolkit's FIND BOUNDARY NUCLEOSOMES script.
# takes a bed file of transcript annotations
# chr \t trxStrt \t trxEnd \t Name \t directionalStart \n
#
# and appends to the end
# "+" \t " startDyad count \t stop dyad count \n"
#
#
# if trxStrt == directionalStart ; +1 strand
# if trxEnd == directionalStart ;-1 strand
# startDyad count is 5' nuc if on +1 strand
# startDyad count is 3' nuc if on -1 strand
#
# ADDED 4/09/12 - need to write strand to output file: galaxy tool
# properly interprets this knowledge, flips information around alignmentpoint.

# this creates a file for making a heat map, computing NRLs, etc.
#############################################################################

import sys

infile = sys.argv[1] #infile .bed
outfile = sys.argv[4] #outfile.bed
upstream = int(sys.argv[2]) # how many bp upstream?
downstream = int(sys.argv[3]) # how many bp downstream?

opin = open(infile, "r")
opout = open(outfile, "w")

for line in opin:
    tab = line.split("\t")
    name = tab[3].strip()
    if tab[0] == "#chr":
        continue
    if tab[6] == "NA":
        continue
    chr = tab[0]
    start = int(float(tab[6]) - upstream)
    stop = int(float(tab[7].strip()) + downstream)
    
    if tab[4] == ".":
        strand = tab[5]
        if strand  == "+":
            alignpt = str(tab[6])
        
        if strand  == "-":
            alignpt = str(tab[7].strip())
    if tab[4] != tab[1] or tab[2]:
    	strand = tab[5]
    	if strand =="+":
    		alignpt = str(tab[6])
    	if strand == "-":
    		alignpt = str(tab[7].strip())
    else:
        if float(tab[1]) == float(tab[4]):
            strand = "+"
            alignpt = str(tab[6])
        if float(tab[2]) == float(tab[4]):
            strand = "-"
            alignpt = str(tab[7].strip())
    output = [chr, str(start), str(stop), name, alignpt, strand)
    for item in output:
        opout.write(item)
        opout.write("\t")
    opout.write("\n")
   

opin.close()
opout.close()
