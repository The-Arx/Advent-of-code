from DataGetter import getData

year=2020
day=7

txt=getData(year,day)
#replace statments go here

lines=txt.split("\n")

children={}
parents={}

for line in lines:
  print(line)
  container,contents=line.split(" contain ")
  container=container.split(" bag")[0]
  contents=contents.split(".")[0]
  children[container]=[]
  if contents=="no other bags":
    continue
  contents=contents.split(", ")
  for child in contents:
    child=child.split(" bag")[0]
    num,bag=child.split(" ",1)
    num=int(num)
    children[container].append([num,bag])
    if bag in parents:
      parents[bag].append(container)
    else:
      parents[bag]=[container]
      
tested=set();
def findParents(bag):
  if bag in parents:
    for parent in parents[bag]:
      if not (parent in tested):
        tested.add(parent)
        findParents(parent)
def findChildCount(bag):
  num=0
  for child in children[bag]:
    num+=child[0]*(1+findChildCount(child[1]))
  return num
findParents("shiny gold")
print(len(tested))
print(findChildCount("shiny gold"))


