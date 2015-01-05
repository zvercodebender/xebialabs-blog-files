from __future__ import with_statement
import sys
import com.xebialabs.deployit.plugin.api.udm.Parameters
from overtherepy import OverthereHostSession, StringUtils
import logger

logger.info("Loading..... compare_deployed_files.py")

class list_all_files:


class diff2repo:

   def GET( self, deployed ):
      logger.error("======== Get Diffs ===========");


   def TEST( self, deployed ):
      for d in deployed:
          dtype = str(d.deployable.type)
          if dtype == "file.File" or dtype == "file.Folder":
              if dtype == "file.File":
                  #print "%s/%s " % (d.targetPath, d.name)
                  remote_path = "%s/%s" % (d.targetPath, d.name)
              else:
                  #print "%s/ " % (d.targetPath)
                  remote_path = d.targetPath
              # End if
              with OverthereHostSession(d.container) as session:
                  diff_lines = remote_diff(session, d.file, remote_path)
                  logger.info("+--------------------------------------------")
                  logger.info("|         %s on %s" % (d.name, d.container))
                  logger.info("+--------------------------------------------")
              if len(diff_lines) > 0:
                  #print "%s" % (diff_lines)
                  logger.info(StringUtils.concat(diff_lines))
              # End if
              logger.info("+--------------------------------------------")
          # End if  
      # End for
   # End Def


   def remote_diff(session, source_file, remote_path):
       #logger.info(remote_path)
       if source_file.isDirectory():
           t = session.work_dir_file("tmp")
       else:
           t = session.work_dir_file(source_file.name)
       session.copy_to(source_file, t)
       response = session.execute("diff %s %s" % (t.path, remote_path), check_success=False)
       return response.stdout
   # End Def

