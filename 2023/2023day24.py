from DataGetter import getData

year = 2023
day = 24

txt='''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''

txt=getData(year, day)

def findIntersect(stone1,stone2):
  [x1,y1,z1],[dx1,dy1,dz1]=stone1
  [x2,y2,z2],[dx2,dy2,dz2]=stone2
  top = -dy1*x1 - dx1*y2 + dx1*y1 + dy1*x2
  bottom = dx1*dy2 - dy1*dx2
  if bottom==0:
    return False,None,None
  t2=top/bottom
  t1=(y2 + t2*dy2 - y1) / dy1
  x=x1 + t1*dx1
  #print(x,x2 + t2*dx2)
  #assert abs(x-(x2 + t2*dx2))<1
  y=y1 + t1*dy1
  #assert abs(y-(y2 + t2*dy2))<1
  return t1>=0 and t2>=0,x,y
  

def parseData(txt):
  return [tuple(tuple(map(int,pos.split(", "))) for pos in line.split(" @ ")) for line in txt.split("\n")]

def part1(txt):
  stones=parseData(txt)
  
  for stone in stones:
    for vel in stone[1]:
      assert vel!=0
  
  result = 0
  
  minNum=200000000000000
  maxNum=400000000000000
  
  #minNum=7
  #maxNum=27
  
  for i, stone in enumerate(stones):
    print(stone)
    for j in range(i):
      stone2=stones[j]
      intersect,x,y=findIntersect(stone,stone2)
      if intersect and x>=minNum and y>=minNum and x<=maxNum and y<=maxNum:
        result+=1
  
  return result

print(part1(txt))