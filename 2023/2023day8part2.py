from DataGetter import getData

year = 2023
day = 8

#replace statments go here

txt='''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''
txt=getData(year, day)

instructions,paths=txt.split("\n\n")

paths=paths.split("\n")

data={}

for line in paths:
  name,contents=line.split(" = ")
  contents=contents[1:-1].split(", ")
  data[name]=contents

i=0

oldnodes=[]
nodes=[{'id' : node} for node in data if node.endswith("A")]
#print(nodes)
while len(nodes)>0:
  direction=instructions[i%len(instructions)]
  if direction=='L':
    pick=0
  else:
    pick=1
  i+=1
  for j,node in list(enumerate(nodes)):
    node['id']=data[node['id']][pick]
    if node['id'].endswith('Z'):
      if 'firstz' in node:
        print(i-node['firstz'])
        node['nextz']=i
        nodes.pop(j)
        oldnodes.append(node)
      else:
        node['firstz']=i
  #print(nodes)
    

#print(i)