
# Directory holding the Acts CUDA SeedFinder unit test.
set( ASFD_CUDA_UNITTEST_DIR
   "${CMAKE_SOURCE_DIR}/acts/Tests/UnitTests/Plugins/Cuda/Seeding2" CACHE PATH
   "Directory holding the CUDA SeedFinder unit test." )
mark_as_advanced( ASFD_CUDA_UNITTEST_DIR )

# Look up the necessary external(s).
find_package( Boost COMPONENTS program_options )

# Set up the executable.
add_executable( asfdSpacePointBinning
   "main.cpp" "CommandLineArguments.hpp" "CommandLineArguments.cpp"
   "WriteSeedFile.hpp" "WriteSeedFile.cpp"
   "${ASFD_CUDA_UNITTEST_DIR}/ReadSeedFile.hpp"
   "${ASFD_CUDA_UNITTEST_DIR}/ReadSeedFile.cpp"
   "${ASFD_CUDA_UNITTEST_DIR}/TestSpacePoint.hpp"
   "${ASFD_CUDA_UNITTEST_DIR}/TestSpacePoint.cpp" )
target_include_directories( asfdSpacePointBinning
   PRIVATE "${ASFD_CUDA_UNITTEST_DIR}" )
target_link_libraries( asfdSpacePointBinning
   PRIVATE Boost::program_options ActsCore )
