#!/bin/bash
#
# Script that prepares test files for the seed-finder unit tests using my
# particular directory layout.
#

# Prepare the PU=20 files.
for i in $(seq 1 100);
do
   ./preparePileUpSpacePoints.py \
      -o /data/projects/acts/atlas_seeds/pu20/evt${i}.txt \
      -s /data/acts_data/ttbar/spacepoints_evt${i}.txt \
      --lowPtMinBiasFiles="/data/acts_data/minbias_inelastic_low/spacepoints_evt*.txt" \
      --nLowPtMinBias=20 \
      --highPtMinBiasFiles="/data/acts_data/minbias_inelastic_high/spacepoints_evt*.txt" \
      --nHighPtMinBias=2 -r ${i}
done

# Prepare the PU=40 files.
for i in $(seq 1 100);
do
   ./preparePileUpSpacePoints.py \
      -o /data/projects/acts/atlas_seeds/pu40/evt${i}.txt \
      -s /data/acts_data/ttbar/spacepoints_evt${i}.txt \
      --lowPtMinBiasFiles="/data/acts_data/minbias_inelastic_low/spacepoints_evt*.txt" \
      --nLowPtMinBias=40 \
      --highPtMinBiasFiles="/data/acts_data/minbias_inelastic_high/spacepoints_evt*.txt" \
      --nHighPtMinBias=4 -r ${i}
done

# Prepare the PU=60 files.
for i in $(seq 1 100);
do
   ./preparePileUpSpacePoints.py \
      -o /data/projects/acts/atlas_seeds/pu60/evt${i}.txt \
      -s /data/acts_data/ttbar/spacepoints_evt${i}.txt \
      --lowPtMinBiasFiles="/data/acts_data/minbias_inelastic_low/spacepoints_evt*.txt" \
      --nLowPtMinBias=60 \
      --highPtMinBiasFiles="/data/acts_data/minbias_inelastic_high/spacepoints_evt*.txt" \
      --nHighPtMinBias=6 -r ${i}
done

# Prepare the PU=80 files.
for i in $(seq 1 100);
do
   ./preparePileUpSpacePoints.py \
      -o /data/projects/acts/atlas_seeds/pu80/evt${i}.txt \
      -s /data/acts_data/ttbar/spacepoints_evt${i}.txt \
      --lowPtMinBiasFiles="/data/acts_data/minbias_inelastic_low/spacepoints_evt*.txt" \
      --nLowPtMinBias=80 \
      --highPtMinBiasFiles="/data/acts_data/minbias_inelastic_high/spacepoints_evt*.txt" \
      --nHighPtMinBias=8 -r ${i}
done

# Prepare the PU=100 files.
for i in $(seq 1 100);
do
   ./preparePileUpSpacePoints.py \
      -o /data/projects/acts/atlas_seeds/pu100/evt${i}.txt \
      -s /data/acts_data/ttbar/spacepoints_evt${i}.txt \
      --lowPtMinBiasFiles="/data/acts_data/minbias_inelastic_low/spacepoints_evt*.txt" \
      --nLowPtMinBias=100 \
      --highPtMinBiasFiles="/data/acts_data/minbias_inelastic_high/spacepoints_evt*.txt" \
      --nHighPtMinBias=10 -r ${i}
done

# Prepare the PU=150 files.
for i in $(seq 1 100);
do
   ./preparePileUpSpacePoints.py \
      -o /data/projects/acts/atlas_seeds/pu150/evt${i}.txt \
      -s /data/acts_data/ttbar/spacepoints_evt${i}.txt \
      --lowPtMinBiasFiles="/data/acts_data/minbias_inelastic_low/spacepoints_evt*.txt" \
      --nLowPtMinBias=150 \
      --highPtMinBiasFiles="/data/acts_data/minbias_inelastic_high/spacepoints_evt*.txt" \
      --nHighPtMinBias=15 -r ${i}
done

# Prepare the PU=200 files.
for i in $(seq 1 100);
do
   ./preparePileUpSpacePoints.py \
      -o /data/projects/acts/atlas_seeds/pu200/evt${i}.txt \
      -s /data/acts_data/ttbar/spacepoints_evt${i}.txt \
      --lowPtMinBiasFiles="/data/acts_data/minbias_inelastic_low/spacepoints_evt*.txt" \
      --nLowPtMinBias=200 \
      --highPtMinBiasFiles="/data/acts_data/minbias_inelastic_high/spacepoints_evt*.txt" \
      --nHighPtMinBias=20 -r ${i}
done
