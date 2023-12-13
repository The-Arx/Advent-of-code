from DataGetter import getData

year = 2022
day = 8


txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

result = 0
visible=[[False]*len(lines[i]) for i in range(len(lines))]


for i in range(len(lines)):
  line = lines[i]
  highest='/'
  for j in range(len(line)):
    char = line[j]
    if char>highest:
      highest=char
      if not visible[i][j]:
        result+=1
        visible[i][j]=True

for i in range(len(lines)):
  line = lines[i]
  highest='/'
  for j in reversed(range(len(line))):
    char = line[j]
    if char>highest:
      highest=char
      if not visible[i][j]:
        result+=1
        visible[i][j]=True
        
for j in range(len(lines[0])):
  highest='/'
  for i in range(len(lines)):
    char = lines[i][j]
    if char>highest:
      highest=char
      if not visible[i][j]:
        result+=1
        visible[i][j]=True
          
for j in range(len(lines[0])):
  highest='/'
  for i in reversed(range(len(lines))):
    char = lines[i][j]
    if char>highest:
      highest=char
      if not visible[i][j]:
        result+=1
        visible[i][j]=True      
      


print(result)