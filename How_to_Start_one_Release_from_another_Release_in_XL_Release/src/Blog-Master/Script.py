import com.xebialabs.xlrelease.api.v1.forms

def gatesBeforeTask(task):
  gatesList = []
  for item in phase.tasks:
    if str(item.getTaskType()) == "xlrelease.GateTask":
     gatesList.append(item)
    if item.id == task.id:
     break
  return gatesList

gates = gatesBeforeTask(task)
conditions = gates[0].getConditions()

for condition in conditions:
 if condition.title == "isDistributed" and condition.isChecked():
    templateName="Blog-Distributed"
    template = templateApi.getTemplates( templateName )
    print "Name = %s \n" % templateName
    print "ID   = %s \n" % template[0].id
    sr = StartRelease()
    sr.setReleaseTitle("New Distributed")
    sr.releaseVariables={"myvar":"1"}
    r = templateApi.start(template[0].id, sr)
    print "Release ID = %s \n" % release.id


 if condition.title == "isMainframe" and condition.isChecked():
    templateName="Blog-Mainframe"
    template = templateApi.getTemplates( templateName )
    print "Name = %s \n" % templateName
    print "ID   = %s \n" % template[0].id
    sr = StartRelease()
    sr.setReleaseTitle("New Mainframe")
    sr.releaseVariables={"yourvar":"1"}
    r = templateApi.start(template[0].id, sr)
    print "Release ID = %s \n" % release.id

