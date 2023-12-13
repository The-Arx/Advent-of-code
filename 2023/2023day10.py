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
  ".":()
}


for i, line in enumerate(lines):
  if "S" in line:
    nextpos=0
    positions=[]
    for j in range(2):
      positions.append({
        'y':i,
        'x':line.index("S"),
      })
    for d in range(4):
      p=positions[nextpos]
      if canMove(p,d):
        p['dir']=d
        nextpos+=1
        if nextpos>=2:
          break
    break

i=0
going=True
while going:
  i+=1
  for j,pos in enumerate(positions):
    nextMove(pos)
    #print("{}: {}, {}".format(j,pos['x'],pos['y']))
    #if abs(positions[0]['x']-positions[1]['x'])<2 and abs(positions[0]['y']-positions[1]['y'])<2:
      #print("NEAR")
    if positions[0]['x']==positions[1]['x'] and positions[0]['y']==positions[1]['y']:
      if j==0:
        i-=1
      going=False
      break
  
  
print(i)