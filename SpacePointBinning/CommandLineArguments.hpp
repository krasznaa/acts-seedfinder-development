// This file is part of the Acts project.
//
// Copyright (C) 2020 CERN for the benefit of the Acts project
//
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

#pragma once

// System include(s).
#include <cstddef>
#include <string>

/// Structure holding the arguments passed to the test executable on the command
/// line
struct CommandLineArguments {
  /// Input spacepoint file to use
  std::string inputFile = "sp.txt";
  /// Prefix to the output file(s)
  std::string outputPrefix = "spGroup";
  /// Postfix to the output file(s).
  std::string outputPostfix = ".txt";
  /// Look for spacepoint duplicates in the received input file, and remove them
  bool filterDuplicates = false;

  /// Interpret the command line arguments of the test executable
  void interpret(int argc, char* argv[]);

};  // struct CommandLineArguments
