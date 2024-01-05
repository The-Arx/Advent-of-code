from DataGetter import getData

year = 2023
day = 22

txt="""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

txt=getData(year, day)

def parseData(txt):
  return [[tuple(map(int,pos.split(","))) for pos in line.split("~")] for line in txt.split("\n")]

def overlap(start1,stop1,start2,stop2):
  return start1<=start2<=stop1 or start1<=stop2<=stop1

def intersects(brick1,brick2):
  for i in range(3):
    a1=min(brick1[0][i],brick1[1][i])
    a2=max(brick1[0][i],brick1[1][i])
    b1=min(brick2[0][i],brick2[1][i])
    b2=max(brick2[0][i],brick2[1][i])
    if not overlap(a1,a2,b1,b2):
      return False
  return True

def gravity(bricks):
  maxHeight=[[(0,None)]*10 for _ in range(10)]
  restingOn=[set() for brick in bricks]
  supporting=[set() for brick in bricks]
  bricks.sort(key=lambda brick:min(brick[0][2],brick[1][2]))
  for i,brick in enumerate(bricks):
    [x1,y1,z1],[x2,y2,z2]=brick
    assert x1<=x2
    assert y1<=y2
    assert z1<=z2
    dz=z2-z1+1
    maxz=0
    resting=restingOn[i]
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        z,otherBrickNum=maxHeight[x][y]
        if z>maxz:
          maxz=z
          resting.clear()
        if z==maxz and otherBrickNum is not None:
          resting.add(otherBrickNum)
    z=maxz+dz
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        maxHeight[x][y]=(z,i)
    for otherBrickNum in resting:
      supporting[otherBrickNum].add(i)
          
  return restingOn,supporting

def part1(txt):
  bricks=parseData(txt)
  
  restingOn,supporting=gravity(bricks)
  
  result=0
  
  for i, brick in enumerate(bricks):
    for j in supporting[i]:
      if len(restingOn[j])==1:
        break
      assert len(restingOn[j])>1
    else:
      result+=1
    
  return result
  
def part2(txt):
  bricks=parseData(txt)
  
  restingOn,supporting=gravity(bricks)
  
  #numresting=[None]*len(bricks)
  
  def numResting(brickNum,bricksLeft=None):
    if bricksLeft==None:
      bricksLeft=[True]*len(bricks)
    num=0
    for i in supporting[brickNum]:
      if not bricksLeft[i]:
        continue
      for j in restingOn[i]:
        if bricksLeft[j] and j!=brickNum:
          break
      else:
        bricksLeft[i]=False
        num+=1+numResting(i,bricksLeft)
    
    return num
  
  result=0
  for i in reversed(range(len(bricks))):
    result+=numResting(i)
    
  return result

#20388 too low
print(part2(txt))