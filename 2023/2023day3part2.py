from DataGetter import getData

year=2023
day=3

txt=getData(year,day)
#replace statments go here

world=txt.split("\n")

result=0

def get(y,x):
  if y>=0 and y<len(world) and x>=0 and x<len(world[y]):
    return world[y][x]
  return "."

def getNum(y,x):
  num=""
  i=x
  while get(y,i).isdigit():
    num+=get(y,i)
    i+=1
  i=x-1
  while get(y,i).isdigit():
    num=get(y,i)+num
    i-=1
  return int(num)

def isNum(y,x):
  return get(y,x).isdigit()

#def test(y,x):
#  return isSymbol(y,x) or isSymbol(y+1,x) or isSymbol(y-1,x)

for i in range(len(world)):
  line=world[i]
  print(line)
  #do something
  
  j=0
  while j < len(line):
    #do something
    if line[j]=='*':
      n=0
      p=1
      if isNum(i,j-1):
        n+=1
        p*=getNum(i,j-1)
      if isNum(i,j+1):
        n+=1
        p*=getNum(i,j+1)
      if isNum(i+1,j):
        n+=1
        p*=getNum(i+1,j)
      else:
        if isNum(i+1,j-1):
          n+=1
          p*=getNum(i+1,j-1)
        if isNum(i+1,j+1):
          n+=1
          p*=getNum(i+1,j+1)
      if isNum(i-1,j):
        n+=1
        p*=getNum(i-1,j)
      else:
        if isNum(i-1,j-1):
          n+=1
          p*=getNum(i-1,j-1)
        if isNum(i-1,j+1):
          n+=1
          p*=getNum(i-1,j+1)
      if n==2:
        result+=p
    j+=1

print(result)
