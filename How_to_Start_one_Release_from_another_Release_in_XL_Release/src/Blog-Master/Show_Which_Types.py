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
   print "Condition: " + str(condition.title) + " is : " + str(condition.isChecked()) + "\n"

