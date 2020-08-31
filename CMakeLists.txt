
# Set up the project.
cmake_minimum_required( VERSION 3.13 )
project( ActsSeedfinderDevelopment VERSION 0.0.1 LANGUAGES CXX )

# Set up the Acts code from the included submodule.
add_subdirectory( acts )

# Add this project's subdirectories.
add_subdirectory( SpacePointBinning )
