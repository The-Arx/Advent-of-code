from DataGetter import getData
from collections import defaultdict 

year = 2023
day = 25

txt=getData(year, day)

#edges to cut:
  #pmn-kdc
  #grd-hvm
  #jmn-zfk

def parseData(txt):
  lines=txt.split("\n")
  connections=defaultdict(lambda:[])
  for line in lines:
    name,others=line.split(": ")
    #print(name,others)
    others=others.split(" ")
    for other in others:
      print("{}--{};".format(name,other))
      connections[other].append(name)
      connections[name].append(other)
  return connections

def removeConn(connections,name1,name2):
  connections[name1].pop(connections[name1].index(name2))
  connections[name2].pop(connections[name2].index(name1))
  
def findSize(connections,name,visited=None):
  if visited==None:
    visited=set()
  visited.add(name)
  size=1
  
  for node in connections[name]:
    if not node in visited:
      size+=findSize(connections,node,visited)
  
  return size

def part1(txt):
  global connections
  connections=parseData(txt)
  
  removeConn(connections,"pmn","kdc")
  removeConn(connections,"grd","hvm")
  removeConn(connections,"jmn","zfk")
  
  
  
  
  return findSize(connections,"rgl")*findSize(connections,"cgg")

print(part1(txt))