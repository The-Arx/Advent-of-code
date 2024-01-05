from DataGetter import getData

year = 2023
day = 21

txt="""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

txt=getData(year, day)

lines=txt.split("\n")

for startY,line in enumerate(lines):
  if "S" in line:
    startX=line.index("S")
    break
else:
  assert False
  
positions={(startY,startX)}

moveDiffs=(
  (0,1),
  (0,-1),
  (1,0),
  (-1,0),
)

for i in range(64):
  newPositions=set()
  for y,x in positions:
    for dy,dx in moveDiffs:
      ny=y+dy
      nx=x+dx
      if ny>=0 and nx>=0 and ny<len(lines) and nx<len(lines[y]) and lines[ny][nx]!="#":
        newPositions.add((ny,nx))
  positions=newPositions
  print("\n".join("".join("O" if (i,j) in positions else char for j,char in enumerate(line)) for i,line in enumerate(lines)))
  print()

print(len(positions))


