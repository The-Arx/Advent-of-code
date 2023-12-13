from DataGetter import getData

year=2023
day=5

txt=getData(year,day)
#replace statments go here

items,maps=txt.split("\n\n",1)

items=[{"num":int(item),"type":-1} for item in items.split("seeds: ")[1].split(" ")]

maps=[m.split("\n")[1:] for m in maps.split("\n\n")]

result=0

for i in range(len(maps)):
  m = maps[i]
  #do something
  
  for j in range(len(m)):
    r = m[j]
    print(r)
    dest,source,length = list(map(int,r.split(" ")))
    for k in range(len(items)):
      if source<=items[k]["num"]<source+length and items[k]["type"]<i:
        items[k]['type']=i
        items[k]['num']=dest+items[k]["num"]-source
    #do something
    print('\n'.join(map(str,items)))

print(min(map(lambda item:item["num"],items)))