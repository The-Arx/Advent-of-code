from DataGetter import getData

year=2022
day=25

txt=getData(year,day)
#replace statments go here

lines=txt.split("\n")

digits=['=','-','0','1','2']

result=0

def getSNAFU(num):
  out=""
  while num>0:
    d=(num+2)%5
    out=digits[d]+out
    num=(num+2)//5
  return out

def getDigit(d):
  return digits.index(d)-2
  
def getNum(string):
  num=0
  for c in string:
    num*=5
    num+=getDigit(c)
  return num

for i in range(len(lines)):
  line = lines[i]
  #do something
  
  result+=getNum(line)
    


print(result)
print(getSNAFU(result))