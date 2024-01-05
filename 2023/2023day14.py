from DataGetter import getData

year = 2023
day = 14

txt="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

txt=getData(year, day)

def moveDir(y,x,dy,dx):
  #print(y,x,dy,dx)
  assert lines[y][x]==2
  lines[y][x]=0
  try:
    while y+dy>=0 and x+dx>=0 and lines[y+dy][x+dx]==0:
      y+=dy
      x+=dx
  except IndexError:
    pass
  #print(y,x,lines[9][7])
  lines[y][x]=2
  return (y,x)

def printList(lines,d=None):
  return
  txtdirs=["North","West","South","East"]
  syms=[".","#","O"]
  print("\n".join(["".join(map(lambda char:syms[char],line)) for line in lines]))
  print()
  if d is not None:
    print(i,txtdirs[d])
    
def moveAllDir(dy,dx):
  outer=list(enumerate(lines))
  if dy>0:
    outer=reversed(outer)
  for i, line in outer:
    inner=list(enumerate(line))
    if dx>0:
      inner=reversed(inner)
    #print(list(inner))
    for j, char in inner:
      #print(i,j)
      if char==2:
        ny,nx=moveDir(i,j,dy,dx)
        
def val():
  v=0
  for line in lines:
    for char in line:
      v*=3
      v+=char
  return v

def doCycle(p=True):
  for d in range(4):
    if p:
      printList(lines,d)
    moveAllDir(*dirs[d])
    
def getScore():
  result = 0

  for i,line in enumerate(lines):
    for j,char in enumerate(line):
      if char==2:
        result+=len(lines)-i
        
  return result

lines=[[0 if char=="." else 1 if char=="#" else 2 for char in line] for line in txt.split("\n")]

dirs=(
  (-1,0),
  (0,-1),
  (1,0),
  (0,1),
)

prevStates=set()
i=0
while True:
  doCycle()
  v=val()
  i+=1
  if v in prevStates:
    break
  prevStates.add(v)
  
r=0
while True:
  doCycle()
  r+=1
  if val()==v:
    break

for i in range((10**9-i)%r):
  doCycle()

#moveAllDir(*dirs[i%4])
#i+=1


      
print(getScore())
