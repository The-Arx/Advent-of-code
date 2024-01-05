from DataGetter import getData

year=2022
day=22

txt="""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

#getData(year,day)

board, instructions = txt.split("\n\n")
board = board.split("\n")

facing = 0
y = 0
for x in range(len(board[0])):
  if board[0][x] == '.':
    break
width=max(map(len, board))

def get(y,x):
  return board[y][x] if x < len(board[y]) else ' '

def move(n=1):
  global y
  global x
  print(x, y)
  while n > 0:
    y2, x2 = getMovePos()
    if get(y,x)=='#':
      break
    y=y2
    x=x2
    n -= 1

def getMovePos(y2=None, x2=None):
  if x2 is None:
    x2 = x
  if y2 is None:
    y2 = y
  move = 1 if facing<2 else -1
  if facing % 2 == 0:
    x2 = (x2 + move) % width
  else:
    y2 = (y2 + move) % len(board)
  print(y2,x2)
  if get(y,x) == ' ':
    return getMovePos(y2, x2)
  return (y2, x2)
  

def turn(n):
  global facing
  facing=(facing+n)%4

i=0
while i < len(instructions):
  num = ""
  while i < len(instructions) and instructions[i].isdigit():
    num+=instructions[i]
    i += 1
  move(int(num))
  if i < len(instructions):
    if instructions[i] == 'L':
      turn(-1)
    else:
      turn(1)
    i += 1
print(x*1000+y*4+facing)
 