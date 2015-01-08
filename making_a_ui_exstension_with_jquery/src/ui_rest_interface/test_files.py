import sys
import os
import com.xebialabs.deployit.plugin.api.udm.Parameters

logger.error("Loading..... test_files.py")

logger.error("======== START ===========")
appName="Environments/DEV/fileTest"
ci = repositoryService.read( appName )
for d in ci.deployeds:
    dtype = str(d.type)

    logger.error("dtype = " + dtype)
    if dtype == "file.DeployedFile" or dtype == "file.DeployedFolder":
           
        logger.error("Found a file object we can diff")
        if dtype == "file.DeployedFile":
            logger.error( "TargetPath = " + str(d.targetPath) )
            logger.error( "FileName = " + str(d.name) )
            logger.error( "%s/%s " % ( str(d.targetPath), str(d.name) ) )
        else:
            logger.error( "TargetPath = " + str(d.targetPath) )
            print "%s/ " % ( str(d.targetPath) )
        # End if
    # End if  
# End for


