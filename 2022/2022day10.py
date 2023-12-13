from DataGetter import getData

year = 2022
day = 10

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

result = ""
x = 1

i = 0
target=0
targets=[i for i in range (20,221,40)]
for line in lines:
  if line=="noop":
    dx=0
    di=1
  else:
    dx=int(line.split(" ")[1])
    di=2
  for _ in range(di):
    i+=1
    if x<=i%40<x+3:
      result+="#"
    else:
      result+=" "
    if i%40==0:
      result+="\n"
  x+=dx

print(result)