from DataGetter import getData

year=2023
day=3

txt=getData(year,day)
#replace statments go here

world=txt.split("\n")

result=0

def isSymbol(y,x):
  return y>=0 and y<len(world) and x>=0 and x<len(world[y]) and not world[y][x]=="." and not world[y][x].isdigit()

def test(y,x):
  return isSymbol(y,x) or isSymbol(y+1,x) or isSymbol(y-1,x)

for i in range(len(world)):
  line=world[i]
  print(line)
  #do something
  
  j=0
  while j < len(line):
    #do something
    if line[j].isdigit():
      num=""
      partnum=test(i,j-1)
      while j<len(line) and line[j].isdigit():
        num+=line[j]
        partnum=partnum or test(i,j)
        j+=1
      partnum=partnum or test(i,j)
      if partnum:
        result+=int(num)
    j+=1

print(result)
