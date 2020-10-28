#!/bin/bash
#
# Script that runs the SYCL based seedfinder test on the specified files,
# and saves all the results into a CSV file.
#

# Transmit errors.
set -e

# The spacepoint file names, passed on the command line.
SPACEPOINT_FILES=("$@")

# Loop over the files.
for i in $(seq 0 $((${#SPACEPOINT_FILES[@]}-1))); do
   # The name of the spacepoint file to use.
   spfile=${SPACEPOINT_FILES[$i]}
   # Tell the user what's happening.
   echo -n "Processing file $(($i+1)) / ${#SPACEPOINT_FILES[@]} (${SPACEPOINT_FILES[$i]}) ..."
   # Run the test using the host device.
   #ActsUnitTestSeedfinderSycl -f ${spfile} -m -c -d "SYCL host device" >> seedfinder_host.csv
   # Run the test using the integrated GPU.
   #ActsUnitTestSeedfinderSycl -f ${spfile} -m -c -d "Intel(R) Gen9 HD Graphics NEO" >> seedfinder_igpu.csv
   # Run the test using the NVidia GPU.
   ActsUnitTestSeedfinderSycl -f ${spfile} -m -c -d "GeForce" >> seedfinder_gpu.csv
   # Tell the user that we're done.
   echo " done"
done
