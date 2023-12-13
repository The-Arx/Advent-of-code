from DataGetter import getData

year = 2023
day = 9

txt=getData(year, day)
#replace statments go here

reports=[[int(num) for num in line.split(" ")]for line in txt.split("\n")]

result = 0

def getNextVal(l):
  if l.count(0)==len(l):
    return 0
  diffs=[]
  for i in range(len(l)-1):
    diffs.append(l[i+1]-l[i])
  return l[0]-getNextVal(diffs)

for report in reports:
  result+=getNextVal(report)

print(result)