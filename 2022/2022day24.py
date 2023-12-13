from DataGetter import getData

year = 2022
day = 24

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

tornadoes=[]

arrowToMove={
  '>':(0,1),
  '<':(0,-1),
  'v':(1,0),
  '^':(-1,0),
}

height=len(lines)-2
width=len(lines[0])-2

world=[[0]*width for _ in range(height)]

for i in range(height):
  line=lines[i+1]
  for j in range(width):
    char=line[j+1]
    if char=='.':
      continue
    world[i][j]+=1
    dy,dx=arrowToMove[char]
    tornadoes.append({
      'y':i,
      'x':j,
      'dy':dy,
      'dx':dx,
    })
      
playerpos={(-1,0)}

moves={
  (0,0),
  (1,0),
  (-1,0),
  (0,1),
  (0,-1),
}

result = 0

def moveTornado(t):
  world[t['y']][t['x']]-=1
  t['y']=(t['y']+t['dy'])%height
  t['x']=(t['x']+t['dx'])%width
  world[t['y']][t['x']]+=1
  
def checkMove(pos,dpos):
  y=pos[0]+dpos[0]
  x=pos[1]+dpos[1]
  npos=(y,x)
  global newplayerpos
  if (y==height and x==width-1) or (y==-1 and x==0) or (y>=0 and x>=0 and y<height and x<width and world[y][x]==0):
    newplayerpos.add(npos)

t=0
targets=((height,width-1),(-1,0),(height,width-1))

while True:
  for tornado in tornadoes:
    moveTornado(tornado)
  newplayerpos=set()
  for pos in playerpos:
    for move in moves:
      checkMove(pos,move)
  playerpos=newplayerpos
  result+=1
  if targets[t] in playerpos:
    playerpos={targets[t]}
    t+=1
    if t>=len(targets):
      break

print(result)