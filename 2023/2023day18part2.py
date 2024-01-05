from DataGetter import getData
import re

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

txt=getData(year, day)

lines=txt.split("\n")
data=[]

y=0
x=0

area=0
perimiter=0

for line in lines:
  d=int(line[-2])
  num=int(line[-7:-2],16)
  perimiter+=num
  if d==2 or d==0:
    if d==2:
      dx=-num
    else:
      dx=num
    x+=dx
    area+=dx*y
  elif d==1 or d==3:
    if d==3:
      dy=-num
    else:
      dy=num
    area+=dy#max(dy,0)
    y+=dy
    
assert x==0
assert y==0



print(abs(area)+perimiter//2+1)
