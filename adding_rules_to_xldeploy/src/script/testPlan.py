def getDeploymentGroup():
    print "======================================================================================="
    print "START: getDeploymentGroup"
    # Get our deployed containers
    for delta in deltas.deltas:
        delta_op = str(delta.operation)
        deployed = delta.previous if delta_op == "DESTROY" else delta.deployed
        container = deployed.container
        host = container.host
        depGroup = host.deploymentGroup
        print "Deployment group for %s is %s" % (host, depGroup)
    print "depGroup = %s " % depGroup
    print "END  : getDeploymentGroup"
    print "======================================================================================="
    return depGroup
# End def

def getContainerListFromDeployedApplication():
    print "START: getContainerListFromDeployedApplication"
    containers = {}
    env = deployedApplication.getEnvironment()
    print "ENV = %s" % env.name
    members = env.getMembers()
    for container in members:
        if len( container.host.tags ) > 0 :
           print "Adding %s" % container.host
           containers[container.host] = container
        # End if
    # End if
    print "END  : getContainerListFromDeployedApplication"
    return [containers[ke] for ke in containers.keys()]
# End def
    

def update_hosts(containers, context):
    print "START: update_hosts"
    deploymentGroup = getDeploymentGroup()
    print containers
    for container in containers:
            host = container.host
            dGrp = host.getProperty('deploymentGroup')
            print "Container = %s (%s/%s)"  % (host, dGrp, deploymentGroup)
            if dGrp == deploymentGroup :
                 if 'pretest' in host.tags:
                      context.addStep(steps.os_script(
                         description = "Run the 'greet_user' script on %s" % host,
                         order = 1,
                         target_host = host,
                         script = "script/greet_user",
                         freemarker_context = {"user": "XebiaLabs"}
                     ))
                 if 'posttest' in host.tags:
                      context.addStep(steps.os_script(
                         description = "Run the 'delete_user' script on %s" % host,
                         order = 199,
                         target_host = host,
                         script = "script/greet_user",
                         freemarker_context = {"user": "XebiaLabs"}
                     ))
                 # End if     
            # End if
    print "END  : update_hosts"
# End def
update_hosts( getContainerListFromDeployedApplication(), context )

