#!/usr/bin/env python3
#
# Script translating text files received from Noemi into a form that the
# Acts C++ code understands.
#

# Import the necessary module(s).
import argparse
import csv
import sys

def transcode( inputFileName, outputFileName, mode = 'w' ):
   '''
   Function transcoding one text file from the CSV format that came out of the
   ATLAS simulation, into the format that is expected by the Acts seed-finder
   unit tests.
   '''

   with open( inputFileName, 'r' ) as inputFile:
      spReader = csv.reader( inputFile, delimiter = ',' )
      with open( outputFileName, mode ) as outputFile:
         spWriter = csv.writer( outputFile, delimiter = ' ' )
         for row in spReader:
            spWriter.writerow( [ 'lxyz', 1, row[ 1 ], row[ 2 ], row[ 3 ], 0.05,
                                 0.1 ] )
            pass
         pass
      pass
   return

def main():
   '''
   C(++) style main function for the script.
   '''

   # Parse the command line argument(s).
   parser = argparse.ArgumentParser( description = 'Space point drawer script' )
   parser.add_argument( '-i', '--inputFile',
                        help = 'Input file with spacepoints' )
   parser.add_argument( '-o', '--outputFile',
                        help = 'Output file with spacepoints' )
   args = parser.parse_args()
   print( 'Transcoding %s --> %s' % ( args.inputFile, args.outputFile ) )

   # Perform the transcoding.
   transcode( args.inputFile, args.outputFile )
   return 0

# If the script is being executed directly, run the "main" function.
if __name__ == '__main__':
   sys.exit( main() )
   pass
