from __future__ import with_statement
import sys
import com.xebialabs.deployit.plugin.api.udm.Parameters
from overtherepy import OverthereHostSession, StringUtils

def remote_diff(session, source_file, remote_path):
    #context.logOutput(remote_path)
    if source_file.isDirectory():
        t = session.work_dir_file("tmp")
    else:
        t = session.work_dir_file(source_file.name)
    session.copy_to(source_file, t)
    response = session.execute("diff %s %s" % (t.path, remote_path), check_success=False)
    return response.stdout
# End Def

for d in thisCi.deployeds:
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
        context.logOutput("+--------------------------------------------")
        context.logOutput("|         %s on %s" % (d.name, d.container))
        context.logOutput("+--------------------------------------------")
        if len(diff_lines) > 0:
            #print "%s" % (diff_lines)
            context.logOutput(StringUtils.concat(diff_lines))
        # End if
        context.logOutput("+--------------------------------------------")
    # End if  
# End for
