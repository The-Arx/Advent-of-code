from DataGetter import getData
import re

year=2022
day=5

txt=getData(year,day)
#replace statments go here

setup,lines = [item.split("\n") for item in txt.split("\n\n")]

crates=[[setup[j][i] for j in reversed(range(0,len(setup)-1)) if setup[j][i]!=" "] for i in range(1,len(setup[0]),4)]

def move(num,f,to):
  print("a")
  print(len(crates[f-1][-num:]))
  print(crates[f-1][-num:],"\n")
  any(crates[to-1].append(item) for item in crates[f-1][-num:])
  crates[f-1]=crates[f-1][:-num]
  #for i in range(num):
    #crates[to-1].append(crates[f-1].pop())

result=0

for i in range(len(lines)):
  line = lines[i]
  n,f,t=map(int,re.search("move (\d+) from (\d+) to (\d+)",line).groups())
  print("\n".join(map(str,crates)))
  print(line)
  move(n,f,t)

print("".join(map(lambda a:a[-1],crates)))