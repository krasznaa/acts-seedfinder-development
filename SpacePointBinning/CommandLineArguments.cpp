// This file is part of the Acts project.
//
// Copyright (C) 2020 CERN for the benefit of the Acts project
//
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

// Local include(s).
#include "CommandLineArguments.hpp"

// Boost include(s).
#include <boost/program_options.hpp>

// System include(s).
#include <cstdlib>
#include <iostream>
#include <string>

/// Convenience declaration for using the boost::program_options namespace
namespace po = boost::program_options;

void CommandLineArguments::interpret( int argc, char* argv[] ) {

   // Declare the supported options.
   po::options_description desc("ASFD SpacePoint Binning");
   desc.add_options()
      ( "help,h", "Produce a help message" )
      ( "inputFile,i", po::value< std::string >()->default_value( "sp.txt" ),
        "SpacePoint text file name" )
      ( "outputPrefix,o", po::value< std::string >()->default_value( "spGroup" ),
        "Prefix for the output file(s)" )
      ( "outputPostfix", po::value< std::string >()->default_value( ".txt" ),
        "Postfix for the output file(s)" )
      ( "filterDuplicates,d", po::bool_switch(),
        "Look for spacepoint duplicates in the input file, and remove them "
        "(slow!)" );

   // Parse the command line arguments.
   po::variables_map vm;
   po::store( po::parse_command_line( argc, argv, desc ), vm );
   po::notify( vm );

   // Handle the --help flag.
   if( vm.count( "help" ) ) {
      std::cout << desc << std::endl;
      exit( 0 );
   }

   // Store the arguments in the member variables.
   inputFile = vm[ "inputFile" ].as< std::string >();
   outputPrefix = vm[ "outputPrefix" ].as< std::string >();
   outputPostfix = vm[ "outputPostfix" ].as< std::string >();
   filterDuplicates = vm[ "filterDuplicates" ].as< bool >();
   return;
}
