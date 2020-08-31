
#pragma once

// Acts unit test include(s).
#include "TestSpacePoint.hpp"

// Acts include(s).
#include "Acts/Seeding/BinnedSPGroup.hpp"

// System include(s).
#include <string>

/// Function used to write space points to an output text file
void writeSeedFile( Acts::Neighborhood< TestSpacePoint > spacepoints,
                    const std::string& fileName );
