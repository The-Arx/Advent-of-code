import curses
import time
from DataGetter import getData

year = 2023
day = 10

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

def moveToDir(dy,dx):
  if dx==1:
    return 0
  if dx==-1:
    return 2
  if dy==1:
    return 1
  if dy==-1:
    return 3
  
def dirToMove(d):
  if d==0:
    return (0,1)
  if d==1:
    return (1,0)
  if d==2:
    return (0,-1)
  if d==3:
    return (-1,0)
  
def get(y,x):
  if x<0 or y<0 or y>len(lines) or x>len(lines[y]):
    return "."
  return lines[y][x]

def getRelative(pos,dy,dx):
  return get(pos['y']+dy,pos['x']+dx)

def canMove(pos,d=None):
  if d==None:
    d=pos['dir']
  dpos=dirToMove(d)
  return (d+2)%4 in tubes[getRelative(pos,*dpos)]
  
def nextMove(pos):
  dy,dx=dirToMove(pos['dir'])
  pos['y']+=dy
  pos['x']+=dx
  dirs=tubes[get(pos['y'],pos['x'])]
  pos['dir']=dirs[1-dirs.index((pos['dir']+2)%4)]

tubes={
  "|":(1,3),
  "-":(0,2),
  "L":(3,0),
  "F":(0,1),
  "J":(2,3),
  "7":(1,2),
  ".":()
}


for i, line in enumerate(lines):
  if "S" in line:
    nextpos=0
    startY=i
    startX=line.index("S")
    positions=[]
    for j in range(2):
      positions.append({
        'y':i,
        'x':line.index("S"),
      })
    for d in range(4):
      p=positions[nextpos]
      if canMove(p,d):
        p['dir']=d
        nextpos+=1
        if nextpos>=2:
          break
    break

pipes={
  "-":"─",
  "|":"│",
  "7":"┐",
  "F":"┌",
  "J":"┘",
  "L":"└",
  ".":" ",
  "S":"S",
}

def main(stdscr):
  curses.init_pair(1, 15, 16)#background
  curses.init_pair(2, 87, 16)#path
  curses.init_pair(3, 16, 46)#start
  curses.init_pair(4, 16, 196)#pointer
  
  
  
  '''for i in range(255):
    curses.init_pair(i+1, i, 16)
    stdscr.addstr(str(i)+" ",curses.color_pair(i+1))
  stdscr.refresh()'''
  
  starty=0
  height=140
  
  stdscr.clear()
  for i in range(starty,starty+height):
    for j,char in enumerate(lines[i]):
      stdscr.addch(i-starty,j,pipes[char],curses.color_pair(1))
  stdscr.refresh()
  
  
  
  i=0
  loop=[[False]*len(line) for line in lines]
  first=True
  while first or positions[0]['x']!=positions[1]['x'] or positions[0]['y']!=positions[1]['y']:
    first=False
    for pos in positions:
      y=pos['y']
      x=pos['x']
      stdscr.addch(y,x,"#",curses.color_pair(4))
    time.sleep(0.01)
    stdscr.refresh()
    i+=1
    for j,pos in enumerate(positions):
      y=pos['y']
      x=pos['x']
      char=lines[y][x]
      if char=="S":
        c=3
      else:
        c=2
      stdscr.addch(y,x,pipes[char],curses.color_pair(c))
      #stdscr.addch(height,0,i,curses.color_pair(1))
      nextMove(pos)
  
    
  
  '''
  for i in range(10):
    stdscr.addstr(i,0,"."*10,curses.color_pair(1))
  for i in range(10):
    stdscr.addstr(i,i,"#",curses.color_pair(2))
        
    stdscr.refresh()
    time.sleep(0.1)
  '''
  
  stdscr.getkey()

curses.wrapper(main)