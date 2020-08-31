
// Local include(s).
#include "CommandLineArguments.hpp"
#include "WriteSeedFile.hpp"

// Acts unit test include(s).
#include "ReadSeedFile.hpp"
#include "TestSpacePoint.hpp"

// Acts include(s).
#include "Acts/Seeding/BinFinder.hpp"
#include "Acts/Seeding/BinnedSPGroup.hpp"

// System include(s).
#include <iostream>

int main( int argc, char* argv[] ) {

   // Parse the command line arguments.
   CommandLineArguments cmdl;
   cmdl.interpret( argc, argv );

   // Read in the seeds from the input text file.
   auto spacepoints = readSeedFile( cmdl.inputFile, cmdl.filterDuplicates );
   std::cout << "Read " << spacepoints.size()
             << " spacepoints from file: " << cmdl.inputFile << std::endl;

   // Create a "view vector" on top of them. This is necessary to be able to pass
   // the objects to the Acts code. While the return type of readSeedFile(...) is
   // useful for simplified memory management...
   std::vector< const TestSpacePoint* > spView;
   spView.reserve( spacepoints.size() );
   for( const auto& sp : spacepoints ) {
      spView.push_back( sp.get() );
   }

   // Create the objects that control how bins are chosen for the spacepoints.
   auto bottomBinFinder =
      std::make_shared< Acts::BinFinder< TestSpacePoint > >();
   auto topBinFinder = std::make_shared< Acts::BinFinder< TestSpacePoint > >();

   // Set up the seedfinder configuration.
   Acts::SeedfinderConfig< TestSpacePoint > sfConfig;
   // silicon detector max
   sfConfig.rMax = 160.;
   sfConfig.deltaRMin = 5.;
   sfConfig.deltaRMax = 160.;
   sfConfig.collisionRegionMin = -250.;
   sfConfig.collisionRegionMax = 250.;
   sfConfig.zMin = -2800.;
   sfConfig.zMax = 2800.;
   sfConfig.maxSeedsPerSpM = 5;
   // 2.7 eta
   sfConfig.cotThetaMax = 7.40627;
   sfConfig.sigmaScattering = 1.00000;
   sfConfig.minPt = 500.;
   sfConfig.bFieldInZ = 0.00199724;
   sfConfig.beamPos = {-.5, -.5};
   sfConfig.impactMax = 10.;

   // Set up the spacepoint grid configuration.
   Acts::SpacePointGridConfig gridConfig;
   gridConfig.bFieldInZ = sfConfig.bFieldInZ;
   gridConfig.minPt = sfConfig.minPt;
   gridConfig.rMax = sfConfig.rMax;
   gridConfig.zMax = sfConfig.zMax;
   gridConfig.zMin = sfConfig.zMin;
   gridConfig.deltaRMax = sfConfig.deltaRMax;
   gridConfig.cotThetaMax = sfConfig.cotThetaMax;

   // Covariance tool, sets covariances per spacepoint as required.
   auto ct = [=]( const TestSpacePoint& sp, float, float,
                  float ) -> Acts::Vector2D {
      return { sp.m_varianceR, sp.m_varianceZ };
   };

   // Create a grid with bin sizes according to the configured geometry, and
   // split the spacepoints into groups according to that grid.
   auto grid =
      Acts::SpacePointGridCreator::createGrid< TestSpacePoint >( gridConfig );
   auto spGroup = Acts::BinnedSPGroup< TestSpacePoint >(
      spView.begin(), spView.end(), ct, bottomBinFinder, topBinFinder,
      std::move( grid ), sfConfig );

   // Loop over all spacepoint groups.
   auto itr = spGroup.begin();
   auto end = spGroup.end();
   for( std::size_t i = 0; itr != end; ++i, ++itr ) {
      writeSeedFile( itr.bottom(), cmdl.outputPrefix + std::to_string( i ) +
                     "Bottom" + cmdl.outputPostfix );
      writeSeedFile( itr.middle(), cmdl.outputPrefix + std::to_string( i ) +
                     "Middle" + cmdl.outputPostfix );
      writeSeedFile( itr.top(), cmdl.outputPrefix + std::to_string( i ) +
                     "Top" + cmdl.outputPostfix );
   }

   return 0;
}
