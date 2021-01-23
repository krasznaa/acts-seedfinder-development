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

def makeTimeProfile( name, title, markerStyle, color ):
   '''Function creating timing TProfile objects in a uniform way
   '''
   result = ROOT.TProfile( name, title, 20, 0.0, 200000.0 )
   result.SetLabelSize( 0.0, "x" )
   result.SetTitleSize( 0.0, "x" )
   result.SetLabelSize( 0.06, "y" )
   result.SetTitleSize( 0.06, "y" )
   result.SetTitleOffset( 0.6, "y" )
   result.SetMarkerStyle( markerStyle )
   result.SetMarkerColor( color )
   result.SetMarkerSize( 2 )
   result.SetLineWidth( 3 )
   result.SetLineColor( color )
   return result

def makeRatioProfile( name, title, markerStyle, color ):
   '''Function creating time ratio TProfile objects in a uniform way
   '''
   result = ROOT.TProfile( name, title, 20, 0.0, 200000.0 )
   result.SetLabelSize( 0.12, "x" )
   result.SetTitleSize( 0.12, "x" )
   result.SetLabelSize( 0.12, "y" )
   result.SetTitleSize( 0.12, "y" )
   result.SetTitleOffset( 0.3, "y" )
   result.SetMarkerStyle( markerStyle )
   result.SetMarkerColor( color )
   result.SetMarkerSize( 2 )
   result.SetLineWidth( 3 )
   result.SetLineColor( color )
   result.GetYaxis().SetNdivisions( 504 )
   return result

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

def drawOption( alreadyDrawn ):
   '''Function helping with the drawing of the profiles
   '''
   if alreadyDrawn:
      return 'SAME'
   else:
      return ''

def main():
   '''C(++) style main function for the script.
   '''

   # Set up the command line arguments.
   parser = argparse.ArgumentParser( description = 'Performance plotter' )
   parser.add_argument( '--syclHostResults',
                        help = 'CSV results from the SYCL code on the Host' )
   parser.add_argument( '--syclCpuResults',
                        help = 'CSV results from the SYCL code on the CPU' )
   parser.add_argument( '--syclIGpuResults',
                        help = 'CSV results from the SYCL code on the iGPU' )
   parser.add_argument( '--syclGpuResults',
                        help = 'CSV results from the SYCL code on the GPU' )
   parser.add_argument( '--cudaGpuResults',
                        help = 'CSV results from the CUDA code on the GPU' )
   args = parser.parse_args()

   # Make sure that at least one file was specified.
   if args.syclHostResults == None and args.syclCpuResults == None and \
      args.syclIGpuResults == None and args.syclGpuResults == None and \
      args.cudaGpuResults == None:
      print( 'You must specify at least one CSV result file!' )
      return 1

   # Set some global ROOT style options.
   ROOT.gStyle.SetOptTitle( False )
   ROOT.gStyle.SetOptStat( False )
   ROOT.gStyle.SetPadRightMargin( 0.05 )
   ROOT.gStyle.SetPadLeftMargin( 0.08 )

   # Select which file to read the CPU results from (they *should* be
   # statistically) identical between all of them.
   cpuResults = None
   if args.syclHostResults != None:
      cpuResults = args.syclHostResults
   elif args.syclCpuResults != None:
      cpuResults = args.syclCpuResults
   elif args.syclIGpuResults != None:
      cpuResults = args.syclIGpuResults
   elif args.syclGpuResults != None:
      cpuResults = args.syclGpuResults
   elif args.cudaGpuResults != None:
      cpuResults = args.cudaGpuResults
   else:
      print( '!!!Internal coding error detected!!!' )
      return 1

   # Create a profile of the CPU code's runtime results.
   cpuTime = makeTimeProfile( 'cpuTime', ';;Runtime [s]', ROOT.kCircle,
                              ROOT.kBlack )
   fillProfile( cpuTime, cpuResults, 3, 0 )
   cpuTime.GetYaxis().SetRangeUser( 0.001, 19.0 )

   # Create the profiles for the SYCL Host runtime results.
   syclHostTime = None
   syclHostRatio = None
   if args.syclHostResults != None:
      syclHostTime = makeTimeProfile( 'syclHostTime', ';;Runtime [s]',
                                      ROOT.kCircle, ROOT.kCyan )
      fillProfile( syclHostTime, args.syclHostResults, 3, 1 )
      syclHostTime.GetYaxis().SetRangeUser( 0.001,
                                            syclHostTime.GetYmax() * 1.05 )
      syclHostRatio = makeRatioProfile( 'syclHostRatio', ';Seeds;Runtime Ratio',
                                        ROOT.kCircle, ROOT.kCyan )
      fillProfile( syclHostTime, args.syclHostResults, 3, 2 )
      pass

   # Create the profiles for the SYCL iGPU runtime results.
   syclIGpuTime = None
   syclIGpuRatio = None
   if args.syclIGpuResults != None:
      syclIGpuTime = makeTimeProfile( 'syclIGpuTime', ';;Runtime [s]',
                                      ROOT.kFullCircle, ROOT.kBlue )
      fillProfile( syclIGpuTime, args.syclIGpuResults, 3, 1 )
      syclIGpuRatio = makeRatioProfile( 'syclIGpuRatio', ';Seeds;Runtime Ratio',
                                        ROOT.kFullCircle, ROOT.kBlue )
      fillProfile( syclIGpuRatio, args.syclIGpuResults, 3, 2 )
      pass

   # Create the profiles for the SYCL GPU runtime results.
   syclGpuTime = None
   syclGpuRatio = None
   if args.syclGpuResults != None:
      syclGpuTime = makeTimeProfile( 'syclGpuTime', ';;Runtime [s]',
                                     ROOT.kFullTriangleUp, ROOT.kGreen )
      fillProfile( syclGpuTime, args.syclGpuResults, 3, 1 )
      syclGpuRatio = makeRatioProfile( 'syclGpuRatio', ';Seeds;Runtime Ratio',
                                       ROOT.kFullTriangleUp, ROOT.kGreen )
      fillProfile( syclGpuRatio, args.syclGpuResults, 3, 2 )
      syclGpuRatio.GetYaxis().SetRangeUser( 0.0, 8.2 )
      pass

   # Set up a canvas to draw on.
   canvas = ROOT.TCanvas( 'canvas', 'Canvas', 1400, 1200 )
   canvas.cd()
   topPad = ROOT.TPad( 'topPad', 'Absolute values pad',
                       0.0, 0.333, 1.0, 1.0 )
   topPad.SetTopMargin( 0.03 )
   topPad.SetBottomMargin( 0.0 )
   topPad.SetLeftMargin( 0.1 )
   topPad.SetRightMargin( 0.08 )
   topPad.Draw()
   bottomPad = ROOT.TPad( 'bottomPad', 'Relative values pad',
                          0.0, 0.0, 1.0, 0.333 )
   bottomPad.SetTopMargin( 0.0 )
   bottomPad.SetBottomMargin( 0.3 )
   bottomPad.SetLeftMargin( 0.1 )
   bottomPad.SetRightMargin( 0.08 )
   bottomPad.Draw()

   # A helper object for drawing (a) line(s).
   lineDrawer = ROOT.TLine()
   lineDrawer.SetLineStyle( ROOT.kDashed )
   lineDrawer.SetLineColor( ROOT.kBlack )
   lineDrawer.SetLineWidth( 2 )

   # Draw the runtime plot.
   topPad.cd()
   if syclHostTime != None:
      syclHostTime.Draw()
      cpuTime.Draw( 'SAME' )
   else:
      cpuTime.Draw()
      pass
   if syclIGpuTime != None:
      syclIGpuTime.Draw( 'SAME' )
      pass
   if syclGpuTime != None:
      syclGpuTime.Draw( 'SAME' )
      pass

   bottomPad.cd()
   alreadyDrawn = False
   if syclGpuRatio != None:
      syclGpuRatio.Draw()
      alreadyDrawn = True
      pass
   if syclIGpuRatio != None:
      syclIGpuRatio.Draw( drawOption( alreadyDrawn ) )
      alreadyDrawn = True
      pass
   if syclHostRatio != None:
      syclHostRatio.Draw( drawOption( alreadyDrawn ) )
      alreadyDrawn = True
      pass

   bottomPad.Update()
   lineDrawer.DrawLine( bottomPad.GetUxmin(), 1.0, bottomPad.GetUxmax(), 1.0 )

   # Add a legend on top of it all.
   topPad.cd()
   legend = ROOT.TLegend( 0.12, 0.7, 0.75, 0.95 )
   legend.AddEntry( cpuTime, 'Intel^{#oright} Core#trademark i7-9900k CPU (original C++)' )
   if syclHostTime != None:
      legend.AddEntry( syclHostTime, 'Intel^{#oright} Core#trademark i7-9900k CPU (SYCL Host)' )
      pass
   if syclIGpuTime != None:
      legend.AddEntry( syclIGpuTime, 'Intel^{#oright} UHD Graphics 630 (SYCL)' )
      pass
   if syclGpuTime != None:
      legend.AddEntry( syclGpuTime, 'NVIDIA^{#oright} GeForce^{#oright} RTX 2060 (SYCL)' )
      pass
   legend.Draw()

   # Save the plot.
   canvas.SaveAs( 'runtimes.png' )

   # Return gracefully.
   return 0

# If the script is being executed directly, run the "main" function.
if __name__ == '__main__':
   sys.exit( main() )
   pass
