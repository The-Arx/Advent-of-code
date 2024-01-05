from DataGetter import getData

year = 2023
day = 23

txt="""#.#####################
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

txt=getData(year, day)

lines=txt.split("\n")

dirToDiff=(
  (0,1),
  (0,-1),
  (1,0),
  (-1,0),
)

def longestPath(y,x,beenTo):
  def canMove(ny,nx):
    if not (ny>=0 and nx>=0 and ny<len(lines) and nx<len(lines[ny]) and not beenTo[ny][nx] and lines[ny][nx]!="#"):
      return False
    char=lines[y][x]
    if char==".":
      return True
    if char=="^":
      return ny<y and nx==x
    if char==">":
      return ny==y and nx>x
    if char=="v":
      return ny>y and nx==x
    if char=="<":
      return ny==y and nx<x
    raise Exception("Unexpected char \"{}\" at x={} and y={}".format(char,x,y))
  beenTo[y][x]=True
  bestLength=0
  for dy,dx in dirToDiff:
    ny=y+dy
    nx=x+dx
    if canMove(ny,nx):
      reachesEnd,length=longestPath(ny,nx,beenTo)
      if reachesEnd and length>bestLength:
        bestLength=length
  beenTo[y][x]=False
  if bestLength==0 and y!=len(lines)-1 and x!=len(lines)-2:
    return False,None
  #if bestLength==0:
    #print(bestLength+1)
    #print("\n".join("".join("O" if been else "." for been in line) for line in beenTo))
  return True,bestLength+1
      

def part1(txt):
  beenTo=[[False]*len(line) for line in lines]
  reachesEnd,length=longestPath(0,1,beenTo)
  assert reachesEnd
  return length-1

print(part1(txt))
