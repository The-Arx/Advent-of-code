from DataGetter import getData
import math

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

#txt=getData(year, day)

lines=txt.split("\n")

#           y,x,h,d,n
positions=[(0,0,0,0,0)]

pastPositions={(0,0):[(0,0,0)]}

dirToDiff=(
  (0,1),
  (1,0),
  (0,-1),
  (-1,0),
)



def add(y,x,h,d,n):
  global result
  if n>3 or result<h:
    return
  p=(y,x)
  if p in pastPositions:
    for h2,d2,n2 in pastPositions[p]:
      if h2>=h and d2==d and n2<=n:
        return
  else:
    pastPositions[p]=[]
  '''for i in range(n+1):
    for j in range(h+1):
      if (x,y,j,d,i) in pastPositions:
        return'''
  if y==len(lines)-1 and x==len(lines[y])-1:
    result=h
    print("---New Best {}---".format(h))
  pastPositions[p].append((h,d,n))
  positions.append((y,x,h,d,n))

i=0
result=math.inf
while i<len(positions):
  y,x,h,d,n = positions[i]
  if i%1000==0:
    print(x,y,h,d,n)
  #print(positions[i])
  for j,[dy,dx] in enumerate(dirToDiff):
    ny=y+dy
    nx=x+dx
    if j==(d+2)%4 or ny<0 or nx<0 or ny>=len(lines) or nx >= len(lines[y]):
      continue
    nh=h+int(lines[ny][nx])
    #print(" ",ny,nx,nh,j)
    if j==d:
      add(ny,nx,nh,d,n+1)
    else:
      add(ny,nx,nh,j,1)
  i+=1
print(result)
#print(min(h for y,x,h,_,_ in positions if y==len(lines)-1 and x==len(lines[y])-1))

