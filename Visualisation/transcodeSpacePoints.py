#!/usr/bin/env python3
#
# Script translating text files received from Noemi into a form that the
# Acts C++ code understands.
#

# Import the necessary module(s).
import argparse
import csv

# Parse the command line argument(s).
parser = argparse.ArgumentParser( description = 'Space point drawer script' )
parser.add_argument( '-i', '--inputFile', help = 'Input file with spacepoints' )
parser.add_argument( '-o', '--outputFile',
                     help = 'Output file with spacepoints' )
args = parser.parse_args()
print( 'Transcoding %s --> %s' % ( args.inputFile, args.outputFile ) )

# Transcode the lines from the input file into the output file one-by-one.
with open( args.inputFile, 'r' ) as inputFile:
   spReader = csv.reader( inputFile, delimiter = ',' )
   with open( args.outputFile, 'w' ) as outputFile:
      spWriter = csv.writer( outputFile, delimiter = ' ' )
      for row in spReader:
         spWriter.writerow( [ 'lxyz', 1, row[ 1 ], row[ 2 ], row[ 3 ], 0.05,
                              0.1 ] )
         pass
      pass
   pass
