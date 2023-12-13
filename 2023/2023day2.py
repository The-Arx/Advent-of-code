from DataGetter import getData

year=2023
day=2

txt=getData(year,day)
#replace statments go here

lines=txt.split("\n")

result=0
colors=["red","green","blue"]
for i in range(len(lines)):
  line=lines[i].split(": ")[1].split("; ")
  #do something
  cubes=[0]*len(colors)
  for game in line:
    
    game=game.split(", ")
    for cube in game:
        [num,color]=cube.split(" ")
        cubes[colors.index(color)]=max(int(num),cubes[colors.index(color)])
  result+=cubes[0]*cubes[1]*cubes[2]
print(result)