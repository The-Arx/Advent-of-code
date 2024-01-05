from DataGetter import getData
import sys

year=2017
day=18

txt=getData(year,day)
#replace statments go here

lines=txt.split("\n")

inums=[0,-1]
registers=[
  {'p':0},
  {'p':1},
]
running=0
sent=[]
recived=[]
first=True

result=0

def get(r):
  register=registers[running]
  if r in register:
    #print(r+" was "+str(register[r]))
    return register[r]
  else:
    #print(r+" was unset (0)")
    return 0

#def setR(p,r,v):
#  registers=registers0 if p==0 else registers1
#  registers[r]=v

def getVal(arg):
  try: 
    return int(arg)
  except ValueError:
    return get(arg)

def fSnd(x):
  if running==1:
    global result
    result+=1
  sent.append(getVal(x))
  
def fSet(x,y):
  register=registers[running]
  register[x]=getVal(y)
  #print(x+" is now "+str(register[x]))

def fAdd(x,y):
  fSet(x,get(x)+getVal(y))
  
def fMul(x,y):
  fSet(x,get(x)*getVal(y))
  
def fMod(x,y):
  fSet(x,get(x)%getVal(y))
  
def fRcv(x):
  global recived
  global sent
  global running
  global first
  if len(recived)>0:
    fSet(x,recived.pop(0))
  elif not first and len(sent)==0:
    print(result)
    sys.exit()
  else:
    first=False
    recived=sent
    sent=[]
    running=1-running
    #print("switched to thread "+str(running))
    inums[running]-=1
    
    
def fJgz(x,y):
  if getVal(x)>0:
    inums[running]+=getVal(y)-1
  
instructions={
  'snd':fSnd,
  'set':fSet,
  'add':fAdd,
  'mul':fMul,
  'mod':fMod,
  'rcv':fRcv,
  'jgz':fJgz,
}

n=0
while True:
  i=inums[running]
  #print("\n"+str(n)+") instruction "+str(i))
  line = lines[i]
  #print(line)
  instruct, *args = line.split(" ")
  instructions[instruct](*args)
  inums[running]+=1
  n+=1
