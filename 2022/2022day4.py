from DataGetter import getData

year=2022
day=4

txt=getData(year,day)
#replace statments go here

lines=txt.split("\n")

result=0

def contains(a,b):
  return a[0]<=b[0] and a[1]>=b[1]

for i in range(len(lines)):
  line = lines[i]
  print(line)
  first, second = line.split(",")
  first = list(map(int, first.split("-")))
  second = list(map(int, second.split("-")))
  print(first,second)
  if contains(first, second) or contains(second, first):
    print(True)
    result+=1

print(result)