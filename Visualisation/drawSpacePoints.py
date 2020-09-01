#!/usr/bin/env python3
#
# Script "blindly" drawing all spacepoints from a single file.
#

# Import the necessary module(s).
import argparse
import csv
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

# Parse the command line argument(s).
parser = argparse.ArgumentParser( description = 'Space point drawer script' )
parser.add_argument( '-i', '--inputFile', help = 'Input file with spacepoints' )
args = parser.parse_args()
print( 'Using input file: %s' % args.inputFile )

# Read in the input file as a csv, into separate x, y, z coordinate lists.
x = []
y = []
z = []
with open( args.inputFile, 'r' ) as csvfile:
   spReader = csv.reader( csvfile, delimiter = ' ' )
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
print( 'Read in %i spacepoints' % len( x ) )

# Create a 3D scatter plot of the spacepoints.
fig = plt.figure()
plot = fig.add_subplot( 111, projection = '3d' )
plot.scatter( z, x, y, c = 'r', marker = 'o' )
plot.set_xlabel( 'Z' )
plot.set_ylabel( 'X' )
plot.set_zlabel( 'Y' )
plt.show()
