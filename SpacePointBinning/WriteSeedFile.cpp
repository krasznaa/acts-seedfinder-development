
// Local include(s).
#include "WriteSeedFile.hpp"

// System include(s).
#include <fstream>

void writeSeedFile( Acts::Neighborhood< TestSpacePoint > spacepoints,
                    const std::string& fileName ) {

   // Open the output file.
   std::ofstream ofile( fileName );

   // Write the x-y-z coordinates of all spacepoints into the output file.
   auto itr = spacepoints.begin();
   auto end = spacepoints.end();
   for( ; itr != end; ++itr ) {
      auto* sp = *itr;
      ofile << sp->x() << ", " << sp->y() << ", " << sp->z() << std::endl;
   }
   return;
}
