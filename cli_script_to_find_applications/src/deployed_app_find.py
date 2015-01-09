import sys
import getopt
import re

def help() :
   print "Find a Deployed Application in a Folder.  Commad line options are as follows:"
   print "   --verbose -v      Debug mode"
   print " "
   print "  --folder -f        The folders to look in.  The 'Environments/' will be added "
   print " "
   print "  --app -a           A pattern to search for in the application name"
# End def

def log( outstr ) :
   global verbose
   
   if verbose : print outstr
# End def

try:
   optList, argList = getopt.getopt(sys.argv[1:], 'vf:a:', ['verbose', 'folder=', 'app='])
except getopt.GetoptError, err:
   help()
   sys.exit(2)
#End try

appName=".*"
folder="Environments/"
verbose=0
for opt, arg in optList:
   if verbose : print opt + " = " + arg
   if opt == '--folder'  or opt == '-f' :
       folder = folder + arg
       log( "Looking for deployed apps in " + folder )
   # End if
   if opt == '--app' or opt == '-a' :
       appName = "Environments.*/.*" + arg
       log( "Looking for app named " + appName )
   # End if
   if opt == '--verbose' or opt == '-v' :
       verbose = 1
       log( "DEBUG On" )
   # End if
# End for

depApp = repository.search("udm.DeployedApplication")

for app in depApp:
   if re.match( folder, app ) :
      if re.search( appName, app ) :
         theApp = repository.read(app)
         name = re.sub("^.*/", "", app)
         version = re.sub("^.*/", "", theApp.version)
         print "------------------------------------------"
         print "Application = " + name
         print "Version     = " + version
         print "Environment = " + theApp.environment
         print "Deployeds:"
         for deployed in theApp.deployeds :
            print "   * " + deployed
         # End for
         print "------------------------------------------"
         print " "
      # End if
   # End if
# End for
