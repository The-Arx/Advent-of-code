from DataGetter import getData

year = 2022
day = 7

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")



path=[]
root={
  "type":"dir",
  "childList":[],
  "childDict":{}
}
folder=root

i = 0
while i < len(lines):
  line = lines[i]
  print(line)
  if line.startswith("$"):
    command = line[2:4]
    if command == 'cd':
      arg = line[5:]
      if arg == "/":
        path=[]
        folder=root
      elif arg == "..":
        path.pop()
        folder=folder['parent']
      else:
        path.append(arg)
        folder=folder['childDict'][arg]
  else:
    size,name=line.split(" ")
    if size=="dir":
      child={
        "type":"dir",
        "childList":[],
        "childDict":{}
      }
    else:
      child={
        "type":"file",
        "size":int(size)
      }
    child['name']=name
    child['parent']=folder
    folder['childList'].append(child)
    folder['childDict'][name]=child
        
  #do something
    
  i += 1

def getSize(item):
  if item['type']=='file':
    return item['size']
  else:
    size=0
    for child in item['childList']:
      size+=getSize(child)
    global result
    if size>=spaceNeeded and result>size:
      result=size
    return size
spaceNeeded=0
result = 0
rootSize=getSize(root)
spaceNeeded=30000000+rootSize-70000000
result = rootSize
getSize(root)
print(result)