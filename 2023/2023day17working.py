from DataGetter import getData
from heapq import heappop,heappush

year = 2023
day = 17

txt="""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

'''
txt="""000
110
000
011
000"""#'''

txt=getData(year, day)

lines=txt.split("\n")

#           y,x,h,d,n
positions=[(0,0,0,0,0,None)]

pastPositions={}

dirToDiff=(
  (0,1),
  (1,0),
  (0,-1),
  (-1,0),
)

def setChar(string,i,char):
  return string[:i]+char+string[i+1:]

def printPath(y,x,d,parent):
  return
  printVal=txt.split("\n")
  printVal=["."*len(line)+" "+line for line in lines]
  nextObj=[None,y,x,d,None,parent]
  arrows=(">","v","<","^")
  while nextObj is not None:
    h,y,x,d,n,nextObj=nextObj
    printVal[y]=setChar(printVal[y],x,arrows[d])
  print("\n".join(printVal))
    

def add(h,y,x,d,n,parent):
  if n>10:
    return
  if y==len(lines)-1 and x==len(lines[y])-1:
    print(h)
    printPath(y,x,j,parent)
  p=(y,x)
  if p in pastPositions:
    for d2,n2 in pastPositions[p]:
      if d2==d and n2<=n:
        return
  else:
    pastPositions[p]=[]
  '''for i in range(n+1):
    for j in range(h+1):
      if (x,y,j,d,i) in pastPositions:
        return'''
  pastPositions[p].append((d,n))
  heappush(positions,(h,y,x,d,n,parent))

while True:
  parent=heappop(positions)
  h,y,x,d,n,_ = parent
  #print("h:",h,"y:",y,"x:",x,"d:",d,"n:",n)
  for j,[dy,dx] in enumerate(dirToDiff):
    ny=y+dy
    nx=x+dx
    if j==(d+2)%4 or ny<0 or nx<0 or ny>=len(lines) or nx >= len(lines[y]):
      continue
    nh=h+int(lines[ny][nx])
    #print(nh,ny,nx,j)
    if j==d:
      add(nh,ny,nx,d,n+1,parent)
    else:
      add(nh,ny,nx,j,1,parent)
#print(min(h for y,x,h,_,_ in positions if y==len(lines)-1 and x==len(lines[y])-1))

