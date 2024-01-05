from DataGetter import getData
import math

year = 2023
day = 20

txt="""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

txt=getData(year, day)


lines=txt.split("\n")

modules={}
inputModules={}
def addInputNodes(name,sendTo):
  for item in sendTo:
    if not item in inputModules:
      inputModules[item]={}
    inputModules[item][name]=False

for i, line in enumerate(lines):
  name,sendTo=line.split(" -> ")
  sendTo=sendTo.split(", ")
  data={
    "sendTo":sendTo
  }
  if name=="broadcaster":
    data['type']="broadcast"
  else:
    prefix=name[0]
    data['type']=prefix
    name=name[1:]
    if prefix=="%":
      data['value']=False
    else:
      assert prefix=="&"
  addInputNodes(name,sendTo)
  modules[name]=data
  #print(line)
  
numHigh=0
numLow=0
def pushButton():
  queue=[("broadcaster",False)]
  i=0
  while i<len(queue):
    pulse(queue,*queue[i])
    i+=1

def pulseAll(queue,names,isHigh,caller=None):
  for name in names:
    queue.append((name,isHigh,caller))

def pulse(queue,name,isHigh,caller=None):
  global numHigh
  global numLow
  if isHigh:
    numHigh+=1
  else:
    numLow+=1
  if name=="rx":
    if not isHigh:
      global rxPressed
      rxPressed=True
  if not name in modules:
    return
  data=modules[name]
  #print(name,data)
  send=True
  sendVal=isHigh
  if data['type']=="broadcast":
    pass
  elif data['type']=="%":
    if isHigh:
      send=False
    else:
      data['value']=not data['value']
      sendVal=data['value']
  else:
    inputModules[name][caller]=isHigh
    if name=="nc":
      for key in inputModules['nc']:
        if inputModules['nc'][key] and not rxInputs[key]:
          rxInputs[key]=presses
      global lastPrint
      if lastPrint!=presses and any(inputModules['nc'].values()):
        print("".join('#' if val else '.' for val in inputModules['nc'].values()),presses,inputModules['nc'])
        lastPrint=presses
    sendVal=False
    for key in inputModules[name]:
      if not inputModules[name][key]:
        sendVal=True
        break
  if send:
    pulseAll(queue,data['sendTo'],sendVal,name)

presses=0
lastPrint=0
rxInputs=dict(inputModules['nc'])
while not all(rxInputs.values()):
  presses+=1
  pushButton()
  
print(math.lcm(*rxInputs.values()))
