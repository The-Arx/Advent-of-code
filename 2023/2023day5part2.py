from DataGetter import getData

year=2023
day=5

txt=getData(year,day)
#replace statments go here

itemsraw,maps=txt.split("\n\n",1)

itemsraw=itemsraw.split("seeds: ")[1].split(" ")

def getParts(item,dest,source,length):
  end=source+length-1
  istart=item['start']
  iend=item['end']
  if iend<source or istart>end:
    return ([],[item])
  moved=[]
  unmoved=[]
  if item['start']<source:
    unmoved.append({
      'start':istart,
      'end':source-1
    })
  if iend>end:
    unmoved.append({
      'start':end+1,
      'end':iend
    })
  moved.append({
    'start':max(source,istart)+dest-source,
    'end':min(end,iend)+dest-source
  })
  return (moved,unmoved)

items=[]
for i in range(0,len(itemsraw),2):
  items.append({
    "start":int(itemsraw[i]),
    "end":int(itemsraw[i])+int(itemsraw[i+1])-1
  })

maps=[m.split("\n")[1:] for m in maps.split("\n\n")]


for i in range(len(maps)):
  m = maps[i]
  moved=[]
  unmoved=items
  for mp in m:
    dest,source,length = list(map(int,mp.split(" ")))
    newunmoved=[]
    for item in unmoved:
      moveditems,unmoveditems=getParts(item,dest,source,length)
      newunmoved.extend(unmoveditems)
      moved.extend(moveditems)
    unmoved=newunmoved
  items=moved+unmoved

print(min(map(lambda item:item["start"],items)))