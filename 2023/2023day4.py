from DataGetter import getData

year=2023
day=4

txt=getData(year,day)
#replace statments go here

lines=txt.split("\n")

result=0
numcards=[1]*len(lines)
for j in range(len(lines)):
  line=lines[j]
  print(line)
  line = line.split(": ")[1]
  ansStr, yours = line.split(" | ")
  
  ans = set()
  
  i=0
  while i<len(ansStr):
    ans.add(ansStr[i:i+2])
    i+=3
  count=0
  i=0
  while i<len(yours):
    if yours[i:i+2] in ans:
      count+=1
    i+=3
  i=0
  print(numcards[j],count,result)
  while i<count and i+j+1<len(lines):
    print(i+j+1,numcards[i+j+1],end=" ")
    numcards[i+j+1]+=numcards[j]
    print(numcards[i+j+1],numcards[i])
    i+=1
  result+=numcards[j]
    

print(sum(numcards))