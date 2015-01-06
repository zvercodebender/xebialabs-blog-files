from __future__ import with_statement
import sys
import com.xebialabs.deployit.plugin.api.udm.Parameters
from overtherepy import OverthereHostSession, StringUtils

logger.error("Loading..... compare_deployed_files.py")

def GET( deployed ):
   logger.error("======== Get Diffs ===========")


def TEST( deployed ):
   logger.error("======== TEST Diffs ===========")
   ci = repositoryService.read( deployed )
   for d in ci.deployeds:
       dtype = str(d.type)

       logger.error("dtype = " + dtype)
       if dtype == "file.DeployedFile" or dtype == "file.Folder":
           logger.error("Found a file object we can diff")
           if dtype == "file.DeployedFile":
               logger.error("Deal with files")
               targetPath=str(d.targetPath)
               logger.error("TargetPath = " + targetPath)
               fileName=str(d.name)
               logger.error("FileName = " + fileName)
               logger.error( "%s/%s " % (targetPath, fileName) )
               remote_path = "%s/%s" % (targetPath, fileName)
           else:
               logger.error("Deal with directories")
               targetPath=repositoryService.read(d).targetPath
               print "%s/ " % (targetPath)
               remote_path = targetPath
           # End if
           logger.error("Connect to overthere host @ " + str(d.container) )
           with OverthereHostSession(d.container) as session:
               diff_lines = remote_diff(session, fileName, remote_path)
               logger.error("+--------------------------------------------")
               logger.error("|         %s on %s" % (d.name, d.container))
               logger.error("+--------------------------------------------")
           if len(diff_lines) > 0:
               print "%s" % (diff_lines)
               logger.error(StringUtils.concat(diff_lines))
               print StringUtils.concat(diff_lines)
           # End if
           logger.error("+--------------------------------------------")
       # End if  
   # End for
# End Def


def remote_diff(session, source_file, remote_path):
    logger.error(remote_path)
    if source_file.isDirectory():
        t = session.work_dir_file("tmp")
    else:
        t = session.work_dir_file(source_file.name)
    session.copy_to(source_file, t)
    response = session.execute("diff %s %s" % (t.path, remote_path), check_success=False)
    return response.stdout
# End Def

root = "Hello World"

root = request.query["root"]

logger.error("root = " + root)
print "root = " + root

appName="Environments/DEV/fileTest"

GET( appName )
TEST( appName )
