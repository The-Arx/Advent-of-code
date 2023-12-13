from DataGetter import getData

year = 2023
day = 10

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

def moveToDir(dy,dx):
  if dx==1:
    return 0
  if dx==-1:
    return 2
  if dy==1:
    return 1
  if dy==-1:
    return 3
  
def dirToMove(d):
  if d==0:
    return (0,1)
  if d==1:
    return (1,0)
  if d==2:
    return (0,-1)
  if d==3:
    return (-1,0)
  
def get(y,x):
  if x<0 or y<0 or y>len(lines) or x>len(lines[y]):
    return "."
  return lines[y][x]

def getRelative(pos,dy,dx):
  return get(pos['y']+dy,pos['x']+dx)

def canMove(pos,d=None):
  if d==None:
    d=pos['dir']
  dpos=dirToMove(d)
  return (d+2)%4 in tubes[getRelative(pos,*dpos)]
  
def nextMove(pos):
  dy,dx=dirToMove(pos['dir'])
  pos['y']+=dy
  pos['x']+=dx
  dirs=tubes[get(pos['y'],pos['x'])]
  pos['dir']=dirs[1-dirs.index((pos['dir']+2)%4)]

tubes={
  "|":(1,3),
  "-":(0,2),
  "L":(3,0),
  "F":(0,1),
  "J":(2,3),
  "7":(1,2),
  ".":(),
  "S":(0,1,2,3)
}


for i, line in enumerate(lines):
  if "S" in line:
    pos={
      'y':i,
      'x':line.index("S"),
    }
    for d in range(4):
      if canMove(pos,d):
        pos['dir']=d
        break
    break

loop=[[False]*len(line) for line in lines]
while True:
  loop[pos['y']][pos['x']]=get(pos['y'],pos['x'])
  nextMove(pos)
  if get(pos['y'],pos['x'])=="S":
    break

def connectsPrev(y,x):
  return 2 in tubes[get(y,x)]


area=0
for i,line in enumerate(loop):
  inside=False
  comefrom=None
  printline=""
  debugline=""
  for j,pipe in enumerate(line):
    #print(i,j,pipe)
    if pipe:
      pipedirs=tubes[pipe]
      if pipe=="-":
        pass
      elif 0 in pipedirs:
        comefrom=pipedirs[1-pipedirs.index(0)]
        inside=not inside
        debugline+=str(comefrom)
      elif 2 in pipedirs:
        debugline+=str(pipedirs[1-pipedirs.index(2)])
        if comefrom==pipedirs[1-pipedirs.index(2)]:
          inside=not inside
      else:
        inside=not inside
      printline+=pipe
    elif inside:
      printline+="#"
      area+=1
    else:
      printline+=" "
    if len(debugline)<=j:
      debugline+=" "
  print(printline)
  #print(debugline)
  
print(area)