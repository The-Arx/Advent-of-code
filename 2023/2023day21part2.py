from DataGetter import getData

year = 2023
day = 21

txt="""\
...........
......##.#.
.###..#..#.
..#.#...#..
....#.#....
.....S.....
.##......#.
.......##..
.##.#.####.
.##...#.##.
..........."""
#10116 after 115 steps

txt="""...
.S.
..."""

txt=getData(year, day)

lines=txt.split("\n")
'''
linesNoS=[]
for i,line in enumerate(lines):
  lineNoS=line.replace("S",".")
  lines[i]=lineNoS*10+line+lineNoS*10
  linesNoS.append(lineNoS*21)
  
lines=linesNoS*10+lines+linesNoS*10
#'''
height=len(lines)
width=len(lines[0])

assert width==height

for middleY,line in enumerate(lines):
  if "S" in line:
    middleX=line.index("S")
    break
else:
  assert False
  
assert middleX==(width-1)/2
assert middleY==(height-1)/2

moveDiffs=(
  (0,1),
  (0,-1),
  (1,0),
  (-1,0),
)

ypositions=(0,middleY,height-1)
xpositions=(0,middleX,width-1)

countOverTime=[[[1] for i in range(3)]for j in range(3)]

for i in range(3):
  for j in range(3):
    startY=ypositions[i]
    startX=xpositions[j]
    pastPositions={(startY,startX)}
    positions=[(startY,startX)]
    counts=countOverTime[i][j]
    while True:
      newPositions=[]
      for y,x in positions:
        for dy,dx in moveDiffs:
          ny=y+dy
          nx=x+dx
          pos=(ny,nx)
          if ny>=0 and nx>=0 and ny<height and nx<width and lines[ny][nx]!="#" and not pos in pastPositions:
            pastPositions.add(pos)
            newPositions.append(pos)
      
      
      newCount=len(newPositions)+(0 if len(counts)==1 else counts[-2])
      if len(counts)>=2 and newCount==counts[-2]:
        #print("\n".join("".join("O" if (i,j) in pastPositions else char for j,char in enumerate(line)) for i,line in enumerate(lines)))
        #print()
        break
      counts.append(newCount)
      positions=newPositions

steps=26501365

result=0

side=(steps-middleX)
vertical=(steps-middleY)

assert side%width==0
assert vertical%height==0

repeat=side//width

result+=countOverTime[1][0][width-1]
result+=countOverTime[1][-1][width-1]
result+=countOverTime[0][1][height-1]
result+=countOverTime[-1][1][height-1]

result+=countOverTime[0][0][middleX-1]*repeat
result+=countOverTime[-1][0][middleX-1]*repeat
result+=countOverTime[0][-1][middleX-1]*repeat
result+=countOverTime[-1][-1][middleX-1]*repeat

result+=countOverTime[0][0][width-1+middleX]*(repeat-1)
result+=countOverTime[-1][0][width-1+middleX]*(repeat-1)
result+=countOverTime[0][-1][width-1+middleX]*(repeat-1)
result+=countOverTime[-1][-1][width-1+middleX]*(repeat-1)


assert steps%2==len(countOverTime[1][1])%2


result+=countOverTime[1][1][-2]*(repeat-1)**2#even
result+=countOverTime[1][1][-1]*repeat**2#odd

print(result)



