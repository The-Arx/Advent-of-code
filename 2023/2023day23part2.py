from DataGetter import getData

year = 2023
day = 23

txt="""\
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

'''
txt="""\
#.#####
#.....#
#.###.#
#...#.#
###.#.#
#...#.#
#.###.#
#.....#
#####.#"""
#'''

'''
txt="""\
#.#####
#.....#
#.###.#
#.#...#
#.#.###
#.#...#
#.###.#
#.....#
#####.#"""
#'''

txt=getData(year, day)

dirToDiff=(
  (0,1),
  (0,-1),
  (1,0),
  (-1,0),
)

def addConnection(nodes,id1,id2,weight=1):
  def helper(id1,id2):
    for connection in nodes[id1]:
      if connection[0]==id2:
        if weight!=1 or connection[1]!=1:
          print("COMBINED EDGES!!!!!!!!!!!!")
          print(id1,id2)
          print(connection[1],weight)
        connection[1]=max(weight,connection[1])
        break
    else:
      nodes[id1].append([id2,weight])
  helper(id1,id2)
  helper(id2,id1)
def removeConnection(nodes,id1,id2):
  def helper(id1,id2):
    for i,connection in enumerate(nodes[id1]):
      if connection[0]==id2:
        nodes[id1].pop(i)
        break
    else:
      raise Exception("Nodes were not connected")
  helper(id1,id2)
  helper(id2,id1)

def getGraph(txt):
  lines=txt.split("\n")
  nodes=[]
  nodemessages=[]
  posToId=[[None]*len(line) for line in lines]
  def canMove(ny,nx):
    return ny>=0 and nx>=0 and ny<len(lines) and nx<len(lines[ny]) and lines[ny][nx]!="#"
  def getId(y,x):
    if posToId[y][x] is None:
      posToId[y][x]=len(nodes)
      nodemessages.append("{}[\nlabel=\"{},{}\"\npos=\"{},{}!\"\n]".format(len(nodes),x,y,x/10,-y/10))
      nodes.append([])
    return posToId[y][x]
  
  for i,line in enumerate(lines):
    for j, char in enumerate(line):
      if char=='#':
        continue
      nodeid=getId(i,j)
      for dy,dx in dirToDiff:
        ny=i+dy
        nx=j+dx
        if canMove(ny,nx):
          assert lines[ny][nx]!="#"
          addConnection(nodes,nodeid,getId(ny,nx))
  return nodes,nodemessages

def simplifyNodes(nodes):
  for i,node in enumerate(nodes):
    #print(node)
    if len(node)==2:
      addConnection(nodes,node[0][0],node[1][0],node[0][1]+node[1][1])
      removeConnection(nodes,i,node[0][0])
      removeConnection(nodes,i,node[0][0])
      nodes[i]=None
  #return [node for node in nodes if node is not None]
  
def longestPath(nodes,beenTo,nodeid,goal):
  if nodeid==goal:
    return True,0,[nodeid]
  bestLength=0
  beenTo[nodeid]=True
  node=nodes[nodeid]
  for connection in node:
    if beenTo[connection[0]]:
      continue
    reachedGoal,length,path=longestPath(nodes,beenTo,connection[0],goal)
    if reachedGoal and length+connection[1]>bestLength:
      bestLength=length+connection[1]
      bestPath=path
  
  beenTo[nodeid]=False
  if bestLength==0:
    return False,None,None
  bestPath.append(nodeid)
  return True,bestLength,bestPath
  

def part2(txt):
  nodes,nodemessages=getGraph(txt)
  
  simplifyNodes(nodes)
  
  print("\n".join(message for i,message in enumerate(nodemessages) if nodes[i] is not None))
  
  print("\n".join("\n".join("{}--{} [label={}];".format(i,*connection) for connection in node if i<connection[0]) for i,node in enumerate(nodes) if node is not None))
  
  beenTo=[False]*len(nodes)
  
  reachedGoal,longest,path=longestPath(nodes,beenTo,0,len(nodes)-1)
  print(path)
  assert reachedGoal
  
  return longest

#4098 too low

print(part2(txt))
