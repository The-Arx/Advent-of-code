from DataGetter import getData

year = 2023
day = 8

txt=getData(year, day)
#replace statments go here

instructions,paths=txt.split("\n\n")

paths=paths.split("\n")

data={}

for line in paths:
  name,contents=line.split(" = ")
  contents=contents[1:-1].split(", ")
  data[name]={'paths':contents}

i=0
node='AAA'
while node!='ZZZ':
  direction=instructions[i%len(instructions)]
  if direction=='L':
    node=data[node]['paths'][0]
  else:
    node=data[node]['paths'][1]
  i+=1

print(i)