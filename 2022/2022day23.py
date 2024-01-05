from DataGetter import getData

year = 2022
day = 23

txt=getData(year, day)

def parseData(txt):
  lines=txt.split("\n")
  elfmap=[[False]*len(line) for line in lines]
  elves=[]
  for i,line in enumerate(lines):
    for j,char in enumerate(line):
      if char=="#":
        elfmap[i][j]=False
        elves.push((i,j))
  return elves,elfmap
        
moves=[
  (1,0),
  (-1,0),
  (0,-1),
  (0,1)
]

def part1(txt):
  elves,elfmap=parseData(txt)
  
  def doTick():
    targets=[elf for elf in elves]
    targetcount={}
    for y,x in elves:
      for dy,dx in moves:
        ny=y+dy
        nx=x+dx
        if dy==0:
          for ty in range(ny-1,ny+2):
        elif dx==0:
          
        else:
          raise Exception("Both dx and dy are not zero: {}, {}".format(dx,xy))
  
  for i in range(10):
    doTick()
  

print(part1(txt))