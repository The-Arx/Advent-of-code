from DataGetter import getData
import math

year = 2023
day = 6

txt=getData(year, day)

#txt=txt.replace(" ","")

times,dists=[[int(num) for num in line.split(":")[1].split(" ") if num!=""] for line in txt.split("\n")]

result = 1

def solveQuadratic(a,b,c):
  half1=-b/(2*a)
  half2=math.sqrt(b**2-4*a*c)/(2*a)
  comb1=half1-half2
  comb2=half1+half2
  return (min(comb1,comb2),max(comb1,comb2))

for i in range(len(times)):
    dist=dists[i]
    time=times[i]
    first,last=solveQuadratic(-1,time,-dist)
    result*=int(last)-int(first)

print(result)

  