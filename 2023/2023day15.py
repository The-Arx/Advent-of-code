from DataGetter import getData

year = 2023
day = 15

txt=getData(year, day)

#txt="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

strings=txt.split(",")

def myHash(string):
  val=0
  for char in string:
    val+=ord(char)
    val*=17
    val%=256
    
  return val

boxes=[[] for _ in range(256)]

for i, operation in enumerate(strings):
  if operation[-1]=="-":
    string=operation[:-1]
    h=myHash(string)
    for i,lens in enumerate(boxes[h]):
      if lens[0]==string:
        boxes[h].pop(i)
        break
    
  else:
    string=operation[:-2]
    focalLen=int(operation[-1])
    h=myHash(string)
    for i,lens in enumerate(boxes[h]):
      if lens[0]==string:
        boxes[h][i]=(string,focalLen)
        break
    else:
      boxes[h].append((string,focalLen))
    

result = 0
    
for i,box in enumerate(boxes):
  for j,lens in enumerate(box):
    result+=(i+1)*(j+1)*lens[1]
  

print(result)
