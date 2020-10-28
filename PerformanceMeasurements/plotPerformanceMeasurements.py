#!/usr/bin/env python
#
# Script producing plots from the measurement values gathered from the SYCL
# based Acts seedfinder code.
#

# Import all necessary module(s).
import ROOT
import argparse
import csv
import sys

def fillProfile( profile, csvFileName, xColumn, yColumn ):
   '''Function used to fill TProfile objects with results from the CSV files
   '''

   # Open the CSV file.
   with open( csvFileName, 'r' ) as csvFile:
      csvReader = csv.reader( csvFile, delimiter = ',' )
      # Iterate over all rows.
      for row in csvReader:
         # Fill the TProfile object with information from the appropriate
         # column(s).
         profile.Fill( float( row[ xColumn ] ), float( row[ yColumn ] ) )
         pass
      pass

   # Return gracefully.
   return

def main():
   '''C(++) style main function for the script.
   '''

   # Set up the command line arguments.
   parser = argparse.ArgumentParser( description = 'Performance plotter' )
   parser.add_argument( '--igpuResults',
                        help = 'CSV results from the integrated gpu tests' )
   parser.add_argument( '--gpuResults',
                        help = 'CSV results from the dedicated gpu tests' )
   args = parser.parse_args()

   # Set some global ROOT style options.
   ROOT.gStyle.SetOptTitle( False )
   ROOT.gStyle.SetOptStat( False )
   ROOT.gStyle.SetPadRightMargin( 0.05 )
   ROOT.gStyle.SetPadLeftMargin( 0.08 )

   # Create a profile of the CPU code's runtime results.
   cpuTime = ROOT.TProfile( 'cpuTime', ';;Runtime [s]',
                            20, 0.0, 200000.0 )
   cpuTime.SetLabelSize( 0.0, "x" )
   cpuTime.SetTitleSize( 0.0, "x" )
   cpuTime.SetLabelSize( 0.03, "y" )
   cpuTime.SetTitleSize( 0.03, "y" )
   cpuTime.SetTitleOffset( 1.0, "y" )
   cpuTime.SetMarkerStyle( ROOT.kCircle )
   cpuTime.SetMarkerColor( ROOT.kBlack )
   cpuTime.SetMarkerSize( 2 )
   cpuTime.SetLineWidth( 3 )
   cpuTime.SetLineColor( ROOT.kBlack )
   fillProfile( cpuTime, args.igpuResults, 3, 0 )
   cpuTime.GetYaxis().SetRangeUser( 0.001, 23.0 )

   # Create a profile of the iGPU's runtime results.
   igpuTime = ROOT.TProfile( 'igpuTime', ';;Runtime [s]',
                             20, 0.0, 200000.0 )
   igpuTime.SetMarkerStyle( ROOT.kFullCircle )
   igpuTime.SetMarkerColor( ROOT.kBlue )
   igpuTime.SetMarkerSize( 2 )
   igpuTime.SetLineWidth( 3 )
   igpuTime.SetLineColor( ROOT.kBlue )
   fillProfile( igpuTime, args.igpuResults, 3, 1 )

   # Create a profile of the GPU's runtime results.
   gpuTime = ROOT.TProfile( 'gpuTime', ';;Runtime [s]',
                            20, 0.0, 200000.0 )
   gpuTime.SetMarkerStyle( ROOT.kFullTriangleUp )
   gpuTime.SetMarkerColor( ROOT.kGreen )
   gpuTime.SetMarkerSize( 2 )
   gpuTime.SetLineWidth( 3 )
   gpuTime.SetLineColor( ROOT.kGreen )
   fillProfile( gpuTime, args.gpuResults, 3, 1 )

   # Create a profile of the iGPU / CPU ratio.
   igpuRatio = ROOT.TProfile( 'igpuRatio', ';Spacepoints;Runtime Ratio',
                              20, 0.0, 200000.0 )
   igpuRatio.SetMarkerStyle( ROOT.kFullCircle )
   igpuRatio.SetMarkerColor( ROOT.kBlue )
   igpuRatio.SetMarkerSize( 2 )
   igpuRatio.SetLineWidth( 3 )
   igpuRatio.SetLineColor( ROOT.kBlue )
   fillProfile( igpuRatio, args.igpuResults, 3, 2 )

   # Create a profile of the GPU / CPU ratio.
   gpuRatio = ROOT.TProfile( 'gpuRatio', ';Spacepoints;Runtime Ratio',
                             20, 0.0, 200000.0 )
   gpuRatio.SetLabelSize( 0.06, "x" )
   gpuRatio.SetTitleSize( 0.06, "x" )
   gpuRatio.SetLabelSize( 0.06, "y" )
   gpuRatio.SetTitleSize( 0.06, "y" )
   gpuRatio.SetTitleOffset( 0.5, "y" )
   gpuRatio.SetMarkerStyle( ROOT.kFullTriangleUp )
   gpuRatio.SetMarkerColor( ROOT.kGreen )
   gpuRatio.SetMarkerSize( 2 )
   gpuRatio.SetLineWidth( 3 )
   gpuRatio.SetLineColor( ROOT.kGreen )
   fillProfile( gpuRatio, args.gpuResults, 3, 2 )
   gpuRatio.GetYaxis().SetRangeUser( 0.0, 2.9 )

   # Set up a canvas to draw on.
   canvas = ROOT.TCanvas( 'canvas', 'Canvas', 1400, 1200 )
   canvas.cd()
   topPad = ROOT.TPad( 'topPad', 'Absolute values pad',
                       0.0, 0.333, 1.0, 1.0 )
   topPad.SetTopMargin( 0.02 )
   topPad.SetBottomMargin( 0.0 )
   topPad.Draw()
   bottomPad = ROOT.TPad( 'bottomPad', 'Relative values pad',
                          0.0, 0.0, 1.0, 0.333 )
   bottomPad.SetTopMargin( 0.0 )
   bottomPad.SetBottomMargin( 0.15 )
   bottomPad.Draw()

   # A helper object for drawing (a) line(s).
   lineDrawer = ROOT.TLine()
   lineDrawer.SetLineStyle( ROOT.kDashed )
   lineDrawer.SetLineColor( ROOT.kBlack )
   lineDrawer.SetLineWidth( 2 )

   # Draw the runtime plot.
   topPad.cd()
   cpuTime.Draw()
   igpuTime.Draw( 'SAME' )
   gpuTime.Draw( 'SAME' )
   bottomPad.cd()
   gpuRatio.Draw()
   bottomPad.Update()
   lineDrawer.DrawLine( bottomPad.GetUxmin(), 1.0, bottomPad.GetUxmax(), 1.0 )
   igpuRatio.Draw( 'SAME' )

   # Add a legend on top of it all.
   topPad.cd()
   legend = ROOT.TLegend( 0.15, 0.7, 0.6, 0.9 )
   legend.AddEntry( cpuTime, 'Intel(R) Core(TM) i7-6700 CPU (original C++)' )
   legend.AddEntry( igpuTime, 'Intel(R) Gen9 HD Graphics NEO' )
   legend.AddEntry( gpuTime, 'NVidia GeForce GTX 960' )
   legend.Draw()

   # Save the plot.
   canvas.SaveAs( 'runtimes.png' )

   # Return gracefully.
   return 0

# If the script is being executed directly, run the "main" function.
if __name__ == '__main__':
   sys.exit( main() )
   pass
