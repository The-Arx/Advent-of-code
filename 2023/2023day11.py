from DataGetter import getData

year = 2023
day = 11

txt="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

galaxies=[]

for i, line in enumerate(lines):
  for j, char in enumerate(line):
    if char=="#":
      galaxies.append([i,j,i,j])

for i,line in enumerate(lines):
  if line.count(".")==len(line):
    for g in galaxies:
      if g[0]>i:
        g[2]+=999999

for j in range(len(lines[0])):
  for i,line in enumerate(lines):
    if line[j]!=".":
      break
  else:
    for g in galaxies:
      if g[1]>j:
        g[3]+=999999
        
result = 0

for i,g1 in enumerate(galaxies):
  for j in range(i+1,len(galaxies)):
    g2=galaxies[j]
    result+=abs(g1[2]-g2[2])
    result+=abs(g1[3]-g2[3])
print(result)