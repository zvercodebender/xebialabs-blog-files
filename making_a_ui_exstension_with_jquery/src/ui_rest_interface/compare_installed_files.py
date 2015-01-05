from __future__ import with_statement
import sys
import com.xebialabs.deployit.plugin.api.udm.Parameters
from overtherepy import OverthereHost, OperatingSystemFamily, LocalConnectionOptions, OverthereHostSession, StringUtils, Diff

def server_diff(hostA, hostB, source_file, remote_path):
    global OverthereHostSession
    global OperatingSystemFamily
    global LocalConnectionOptions
    global ObertherHostSession
    global StringUtils
    global Diff

    #context.logOutput(remote_path)
    localOpts = LocalConnectionOptions(os=OperatingSystemFamily.UNIX)
    local_session =  OverthereHostSession(OverthereHost(localOpts))
    sessionA = OverthereHostSession(hostA)
    sessionB = OverthereHostSession(hostB)
    try:
        d1 = sessionA.remote_file(remote_path)
        local_d1 = local_session.work_dir_file("hostA")
        local_session.copy_to(d1, local_d1)
        myFile = "%s" % (local_d1)
        local_f1 = myFile.split(':')[1]

        d2  = sessionB.remote_file(remote_path)
        local_d2 = local_session.work_dir_file("hostB")
        local_session.copy_to(d2, local_d2)
        myFile = "%s" % (local_d2)
        local_f2 = myFile.split(':')[1]

        response = local_session.execute("diff %s %s" % (local_f1, local_f2), check_success=False)
    finally:
        sessionA.close_conn()
        sessionB.close_conn()
        local_session.close_conn()
    # End try
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
        targets = parameters["targets"]
        if len(targets) > 0 :
            hostA = targets.pop()
            hostB = targets.pop()
            diff_lines = server_diff(hostA, hostB, d.name, remote_path)
            context.logOutput("+-------------------------------------------------")
            context.logOutput("| compare ")
            context.logOutput("| %s @ %s " % (d.name, hostA))
            context.logOutput("| to ")
            context.logOutput("| %s @ %s " % (d.name, hostB))
            context.logOutput("+-------------------------------------------------")
            if len(diff_lines) > 0:
                #context.logOutput("%s" % (diff_lines))
                context.logOutput(StringUtils.concat(diff_lines))
            # End if
            context.logOutput("+-------------------------------------------------")
        # End if
    # End if  
    break
# End for
