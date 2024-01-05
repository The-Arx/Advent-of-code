from DataGetter import getData

year = 2015
day = 1

txt=getData(year, day)


count=0
for i,char in enumerate(txt):
  if char=="(":
    count+=1
  else:
    count-=1
  if count<0:
    break
  
print(i+1)
