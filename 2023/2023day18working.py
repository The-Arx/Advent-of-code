from DataGetter import getData

year = 2023
day = 18

txt="""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


class NegativeList:      
  def __init__(self,setDefault=True,default=lambda i:None):
    self.setDefault=setDefault
    self.default=default
    self.below=[]
    self.above=[]
  def __getitem__(self,index):
    if index<0:
      i=-1-index
      l=self.below
    else:
      i=index
      l=self.above
    try:
      return l[i]
    except IndexError:
      if self.setDefault:
        l[i]=self.default(index)
        return l[i]
      else:
        raise
  def __setitem__(self,index,value):
    if index<0:
      i=-1-index
      l=self.below
    else:
      i=index
      l=self.above
    while i>=len(l):
      l.append(None)
    l[i]=value
  def __len__(self):
    return len(self.below)+len(self.above)

txt=getData(year, day)

lines=txt.split("\n")
data=[]

miny=0
maxy=0
minx=0
maxx=0

for line in lines:
  d,num,color=line.split(" ")
  num=int(num)
  if d=="U":
    miny-=num
    diff=(-1,0)
  elif d=="D":
    maxy+=num
    diff=(1,0)
  elif d=="L":
    minx-=num
    diff=(0,-1)
  else:
    assert d=="R"
    maxx+=num
    diff=(0,1)
  data.append({
    'd':d,
    'diff':diff,
    'num':num,
    'color':color
  })

table=NegativeList(default=lambda i:NegativeList())
y=0
x=0


for instr in data:
  dy,dx=instr['diff']
  for i in range(instr['num']):
    y+=dy
    x+=dx
    #print(y,x)
    table[y][x]=instr['color']

result = 0

for i, line in enumerate(table):
  for first,item in enumerate(line):
    if item is not None:
      break
  else:
    continue
  for last,item in reversed(list(enumerate(line))):
    if item is not None:
      break
  else:
    continue
  result+=last-first+1

print(result)
