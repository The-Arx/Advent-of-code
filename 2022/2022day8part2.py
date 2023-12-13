from DataGetter import getData

year = 2022
day = 8

txt='''30373
25512
65332
33549
35390'''

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

height=len(lines)
width=len(lines[0])

result = 0
visible=[[False]*len(lines[i]) for i in range(len(lines))]

def testDir(y,x,dy,dx):
  h=lines[y][x]
  i=y+dy
  j=x+dx
  trees=0
  while i>=0 and j>=0 and i<height and j<width:
    trees+=1
    if lines[i][j]>=h:
      break;
    i+=dy
    j+=dx
  return trees
  
  
  

def visibilty(y,x):
  return testDir(y,x,-1,0) * testDir(y,x,1,0) * testDir(y,x,0,-1) * testDir(y,x,0,1)
    

for i in range(len(lines)):
  for j in range(len(lines[i])):
    result=max(result,visibilty(i,j))


print(result)