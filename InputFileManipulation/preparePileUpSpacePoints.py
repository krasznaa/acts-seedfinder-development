#!/usr/bin/env python3
#
# Script used to create single text files with a varying number of pileup
# events on top of a hard-scatter event.
#

# Import the necessary module(s).
import argparse
import glob
import random
import sys
from transcodeSpacePoints import transcode

def appendTranscoded( inputFileName, outputFileName ):
   '''
   Function used to append one minimum bias file to the output file. In a
   properly "transcoded" format.
   '''

   with open( outputFileName, 'a' ) as ofile:
      ofile.write( '# File: %s\n' % inputFileName )
      pass
   transcode( inputFileName, outputFileName, 'a' )
   return

def main():
   '''
   C(++) style main function for the script.
   '''

   # Parse the command line argument(s).
   parser = \
      argparse.ArgumentParser( description = 'Space point pileup creator' )
   parser.add_argument( '-s', '--signalFile',
                        help = 'Input file with the signal event' )
   parser.add_argument( '--lowPtMinBiasFiles',
                        help = 'Input file(s) with low-pT minimum bias events' )
   parser.add_argument( '--nLowPtMinBias', type = int,
                        help = 'Number of low-pT minimum bias events to use' )
   parser.add_argument( '--highPtMinBiasFiles',
                        help = 'Input file(s) with high-pT minimum bias events' )
   parser.add_argument( '--nHighPtMinBias', type = int,
                        help = 'Number of high-pT minimum bias events to use' )
   parser.add_argument( '-o', '--outputFile',
                        help = 'Output file with all spacepoints' )
   parser.add_argument( '-r', '--randomSeed', type = int,
                        help = 'Seed for the random number generator' )
   args = parser.parse_args()

   # Set up the random number generator(s).
   random.seed( args.randomSeed )

   # Find all the minimum bias files.
   lowPtMinBiasFiles = glob.glob( args.lowPtMinBiasFiles )
   assert len( lowPtMinBiasFiles ) != 0
   highPtMinBiasFiles = glob.glob( args.highPtMinBiasFiles )
   assert len( highPtMinBiasFiles ) != 0

   # Choose the files to use.
   assert len( lowPtMinBiasFiles ) >= args.nLowPtMinBias
   selectedLowPtMinBiasFiles = random.sample( lowPtMinBiasFiles,
                                              args.nLowPtMinBias )
   assert len( highPtMinBiasFiles ) >= args.nHighPtMinBias
   selectedHighPtMinBiasFiles = random.sample( highPtMinBiasFiles,
                                               args.nHighPtMinBias )

   # Merge the files together.
   with open( args.outputFile, 'w' ) as ofile:
      ofile.write( '# Signal file: %s\n' % args.signalFile )
      pass
   transcode( args.signalFile, args.outputFile, 'a' )
   for minBiasFile in selectedLowPtMinBiasFiles:
      appendTranscoded( minBiasFile, args.outputFile )
      pass
   for minBiasFile in selectedHighPtMinBiasFiles:
      appendTranscoded( minBiasFile, args.outputFile )
      pass

   return 0

# If the script is being executed directly, run the "main" function.
if __name__ == '__main__':
   sys.exit( main() )
   pass
