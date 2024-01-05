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

def getScore(beam):
  allBeams=[beam]
  beamset=set()
  beenTo=[[False]*len(line) for line in lines]
  result = [0]
  
  def addBeam(y,x,dy,dx):
    
    beam=(y,x,dy,dx)
    if not beam in beamset:
      if not beenTo[y][x]:
        beenTo[y][x]=True
        result[0]+=1
      beamset.add(beam)
      allBeams.append(beam)
  
  i=0
  while i<len(allBeams):
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
  return result[0]

best=0
for i in range(len(lines)):
  score=getScore((i,-1,0,1))
  print(score)
  best=max(score,best)
  
for i in range(len(lines)):
  score=getScore((i,len(lines[i]),0,-1))
  print(score)
  best=max(score,best)
  
for i in range(len(lines[0])):
  score=getScore((-1,i,1,0))
  print(score)
  best=max(score,best)
  
for i in range(len(lines)):
  score=getScore((len(lines),i,-1,0))
  print(score)
  best=max(score,best)
  
print("\n",best)
