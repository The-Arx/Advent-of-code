from DataGetter import getData

year = 2023
day = 16

txt=""".|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

txt=getData(year, day)

lines=txt.split("\n")


allBeams=[(0,-1,0,1)]
beenTo=[[False]*len(line) for line in lines]

beenTo[0][0] = True
result = 1

def addBeam(y,x,dy,dx):
  global allBeams
  global result
  beam=(y,x,dy,dx)
  if not beenTo[y][x]:
    beenTo[y][x]=True
    result+=1
  if not beam in allBeams:
    allBeams.append(beam)

i=0
while i<len(allBeams):
  #print()
  #print("\n".join("".join("#" if char else "." for char in line) for line in beenTo))
  y,x,dy,dx=allBeams[i]
  y+=dy
  x+=dx
  if y<0 or x<0 or y>=len(lines) or x>=len(lines[y]):
    i+=1
    continue
  char=lines[y][x]
  if char=="|" and dx!=0:
    addBeam(y,x,1,0)
    addBeam(y,x,-1,0)
  elif char=="-" and dy!=0:
    addBeam(y,x,0,1)
    addBeam(y,x,0,-1)
  elif char=="\\":
    addBeam(y,x,dx,dy)
  elif char=="/":
    addBeam(y,x,-dx,-dy)
  else:
    addBeam(y,x,dy,dx)
  i+=1

print(result)
