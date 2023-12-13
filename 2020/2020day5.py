from DataGetter import getData

year=2020
day=5

txt=getData(year,day)
#replace statments go here

lines=txt.split("\n")
seats=[False]*1024
for i in range(len(lines)):
  line=lines[i]
  minr=0
  maxr=128
  for i in range(7):
    change = (maxr - minr) // 2
    if line[i]=='F':
      maxr -= change
    else:
      minr += change
  minc=0
  maxc=8
  for i in range(3):
    change = (maxc - minc) // 2
    if line[i+7]=='L':
      maxc -= change
    else:
      minc += change
  id=minr * 8 + minc
  seats[id]=True
for i in range(1,len(seats)-1):
  if seats[i-1] and not seats[i] and seats[i+1]:
    print(i)