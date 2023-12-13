from DataGetter import getData

year=2022
day=3

txt=getData(year,day)
#replace statments go here

lines=txt.split("\n")

result=0

def getPriority(c):
  code = ord(c)
  return code-64+26 if code < 95 else code-96
  
i=0
while i < len(lines):
  line = lines[i]
  
  for char in line:
    if char in lines[i+1] and char in lines[i+2]:
      result += getPriority(char)
      break
  i+=3

print(result)