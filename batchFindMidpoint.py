###########################################################
# Tess Jeffers
#
# February 11, 2016
#
# Goal: take modENCODE narrow peak formatted files
# find the midpoint of the peak
# update the 'start' and 'stop' coordinates to +/- 500 bp
#
# syntax: $ batchFindMidpoint.py /full/path/to/files
###########################################################

import sys
import os

def findMid(directory):

    print("Creating new .bed files in: " +  directory)

    for narrowPeak in os.listdir(directory):
        inFile = open(os.path.join(directory, narrowPeak), 'r')
        outName = "midpoints_" + narrowPeak  
        outFile = open(os.path.join(directory, outName), 'w')

        for line in inFile:
            items = line.split('\t')
            midpoint = (int(items[2]) - int(items[1])) // 2
            newStart = midpoint - 500
            newEnd = midpoint + 500
            # ouput format: chr\t start\t end\t name\t midpoint\t strand\n
            output = [items[0], "\t", str(newStart), "\t", str(newEnd), "\t", items[3], "\t", str(midpoint), "\t", "+", "\n"]
            for i in output:
                outFile.write(i)

PATH = os.path.abspath(sys.argv[1])

# main
findMid(PATH)
