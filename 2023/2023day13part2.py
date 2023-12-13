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

def setChar(string,i,char):
  return string[:i]+char+string[i+1:]

def toggle(pattern,y,x):
  pattern[y]=setChar(pattern[y],x,"#" if pattern[y][x]=="." else ".")

def getReflection(p,n=None):
  width=len(p[0])
  height=len(p)
  for i in range(1,height):
    d=min(i,height-i)
    #print(i-d,i,i+d,len(p))
    #print(p[i-d:i],list(reversed(p[i:i+d])))
    if p[i-d:i]==list(reversed(p[i:i+d])) and i*100!=n:
      return i*100
  p=tuple(zip(*p))
  for i in range(1,width):
    d=min(i,width-i)
    #print(i-d,i,i+d,len(p))
    #print(p[i-d:i],tuple(reversed(p[i:i+d])))
    if p[i-d:i]==tuple(reversed(p[i:i+d])) and i!=n:
      return i

def getSmudgeReflection(pattern):
  r=getReflection(pattern)
  print(r)
  for y in range(len(pattern)):
    for x in range(len(pattern[0])):
      toggle(pattern,y,x)
      #print("\n".join(pattern))
      newr=getReflection(pattern,r)
      toggle(pattern,y,x)
      #print(y,x,r,newr)
      if newr is not None:
        assert r!=newr
        return newr
  return ":("

for i,pattern in enumerate(patterns):
    result+=getSmudgeReflection(pattern)
  

print(result)