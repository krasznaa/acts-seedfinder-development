#!/usr/bin/env python3
#
# Script drawing bottom-middle-top spacepoints corresponding to the same
# SpacePoint group.
#

# Import the necessary module(s).
import argparse
import csv
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

# Parse the command line argument(s).
parser = argparse.ArgumentParser( description = 'Space point drawer script' )
parser.add_argument( '-b', '--bottom',
                     help = 'Input file with the "bottom" spacepoints' )
parser.add_argument( '-m', '--middle',
                     help = 'Input file with the "middle" spacepoints' )
parser.add_argument( '-t', '--top',
                     help = 'Input file with the "top" spacepoints' )
args = parser.parse_args()
print( 'Using input files:' )
print( '  - bottom: %s' % args.bottom )
print( '  - middle: %s' % args.middle )
print( '  - top   : %s' % args.top )

# Function used to read in one CSV file.
def readSpacePointFile( inputFile ):
   x = []
   y = []
   z = []
   with open( inputFile, 'r' ) as csvFile:
      spReader = csv.reader( csvFile, delimiter = ' ' )
      for row in spReader:
         if row[ 0 ] == '#':
            continue
         elif row[ 0 ] == 'lxyz':
            x += [ float( row[ 2 ] ) ]
            y += [ float( row[ 3 ] ) ]
            z += [ float( row[ 4 ] ) ]
         else:
            x += [ float( row[ 0 ] ) ]
            y += [ float( row[ 1 ] ) ]
            z += [ float( row[ 2 ] ) ]
         pass
      pass
   assert len( x ) == len( y )
   assert len( x ) == len( z )
   print( 'Read in %i spacepoints from %s' % ( len( x ), inputFile ) )
   return ( x, y, z )

# Read in the spacepoints.
bottomSPs = readSpacePointFile( args.bottom )
middleSPs = readSpacePointFile( args.middle )
topSPs    = readSpacePointFile( args.top )

# Create a 3D scatter plot with all 3 types.
fig = plt.figure()
plot = fig.add_subplot( 111, projection = '3d' )
plot.scatter( bottomSPs[ 0 ], bottomSPs[ 1 ], bottomSPs[ 2 ],
              c = 'b', marker = 'o' )
plot.scatter( middleSPs[ 0 ], middleSPs[ 1 ], middleSPs[ 2 ],
              c = 'g', marker = 'o' )
plot.scatter( topSPs[ 0 ], topSPs[ 1 ], topSPs[ 2 ],
              c = 'r', marker = 'o' )
plot.set_xlabel( 'X' )
plot.set_ylabel( 'Y' )
plot.set_zlabel( 'Z' )
plt.show()
