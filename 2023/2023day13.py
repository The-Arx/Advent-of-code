from DataGetter import getData

year = 2023
day = 13

txt="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

txt=getData(year, day)
#replace statments go here

patterns=[pattern.split("\n") for pattern in txt.split("\n\n")]

result = 0

def getReflection(p):
  width=len(p[0])
  height=len(p)
  for i in range(1,height):
    d=min(i,height-i)
    #print(i-d,i,i+d,len(p))
    #print(p[i-d:i],list(reversed(p[i:i+d])))
    if p[i-d:i]==list(reversed(p[i:i+d])):
      return i*100
  p=tuple(zip(*p))
  for i in range(1,width):
    d=min(i,width-i)
    #print(i-d,i,i+d,len(p))
    #print(p[i-d:i],tuple(reversed(p[i:i+d])))
    if p[i-d:i]==tuple(reversed(p[i:i+d])):
      return i

for i,pattern in enumerate(patterns):
  result+=getReflection(pattern)
  

print(result)