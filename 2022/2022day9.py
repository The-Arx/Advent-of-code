from DataGetter import getData

year = 2022
day = 9

txt='''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

txt=getData(year, day)
#replace statments go here



instructions=[line.split(" ") for line in txt.split("\n")]

knots=[[0,0] for i in range(10)]
h=knots[0]
t=knots[-1]

result = 1
beenTo={0:{0}}

def updateBeen(pos):
  if not pos[0] in beenTo:
    beenTo[pos[0]]=set()
  if not pos[1] in beenTo[pos[0]]:
    beenTo[pos[0]].add(pos[1])
    global result
    result+=1
    
def updateBack(f,b):
  if abs(f[0]-b[0])>1 or abs(f[1]-b[1])>1:
    if b[0]<f[0]:
      b[0]+=1
    elif b[0]>f[0]:
      b[0]-=1
    if b[1]<f[1]:
      b[1]+=1
    elif b[1]>f[1]:
      b[1]-=1
    

instructToDiff={
  'U':(0,1),
  'D':(0,-1),
  'L':(-1,0),
  'R':(1,0),
}

def setChar(string,index,char):
  return string[:index]+char+string[index+1:]

def printPos(minx=-5,xlen=11,miny=-5,ylen=11):
  maxx=minx+xlen-1
  maxy=miny+ylen-1
  if minx<=0 and maxx>=0:
    line="."*-miny+"|"+"."*maxx
  else:
    line="."*xlen
  world=[line]*ylen
  if miny<=0 and maxy>=0:
    world[-miny]="-"*xlen
  for i,knot in enumerate(reversed(knots)):
    world[knot[1]-miny]=setChar(world[knot[1]-miny],knot[0]-minx,str(i))
  world[h[1]-miny]=setChar(world[h[1]-miny],h[0]-minx,"H")
  
  
  print("\n".join(reversed(world)))

for instruct in instructions:
  dx,dy=instructToDiff[instruct[0]]
  print(instruct)
  for i in range(int(instruct[1])):
    h[0]+=dx
    h[1]+=dy
    for i in range(len(knots)-1):
      updateBack(knots[i],knots[i+1])
    updateBeen(t)
    #print(h,t,result)
    #printPos()



print(result)