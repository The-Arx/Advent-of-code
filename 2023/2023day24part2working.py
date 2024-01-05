from DataGetter import getData
import scipy.optimize
from matplotlib import pyplot as plt
import numpy as np
from fractions import Fraction

year = 2023
day = 24

txt='''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''

txt=getData(year, day)

'''
def findIntersect(stone1,stone2):
  [x1,y1,z1],[dx1,dy1,dz1]=stone1
  [x2,y2,z2],[dx2,dy2,dz2]=stone2
  top = -dy1*x1 - dx1*y2 + dx1*y1 + dy1*x2
  bottom = dx1*dy2 - dy1*dx2
  if bottom==0:
    return False,None,None
  t2=top/bottom
  t1=(y2 + t2*dy2 - y1) / dy1
  x=x1 + t1*dx1
  #print(x,x2 + t2*dx2)
  #assert abs(x-(x2 + t2*dx2))<1
  y=y1 + t1*dy1
  #assert abs(y-(y2 + t2*dy2))<1
  return t1>=0 and t2>=0,x,y
 ''' 

def parseData(txt):
  return [tuple(tuple(map(int,pos.split(", "))) for pos in line.split(" @ ")) for line in txt.split("\n")]

def findClosest(s0,s1):
  a=tuple(s0[0][i]-s1[0][i] for i in range(3))
  b=tuple(s0[1][i]-s1[1][i] for i in range(3))
  p=sum(vel**2 for vel in b)
  q=sum(a[i]*b[i] for i in range(3))
  r=sum(pos**2 for pos in a)
  if p==0:
    return r
  t=-q/p
  return -q**2/p+r

def part2(txt):
  stones=parseData(txt)
  
  scaling=10**14
  
  for stone in stones:
    for vel in stone[1]:
      assert vel!=0
  
  global globalf
  def f(rock):
    assert len(rock)==6
    rock=(list(map(lambda x:x*scaling,rock[:3])),rock[3:])
    
    totalDist=0
    for stone in stones:
      totalDist+=findClosest(rock,stone)
      
    return totalDist/scaling**2

  globalf=f
  
  
  rock=scipy.optimize.minimize(f,(10,0,0,0,0,0))
  print(rock)
  rv=tuple(map(round,rock['x'][3:]))
  #remove me
  #assert rv==(-336,29,38)
  
  s0=stones[0]
  s1=stones[1]
  
  a=tuple(s0[1][i]-rv[i] for i in range(3))
  b=tuple(-(s1[1][i]-rv[i]) for i in range(3))
  c=tuple(-(s0[0][i]-s1[0][i]) for i in range(3))
  top=c[0]*b[1]-b[0]*c[1]
  bottom=a[0]*b[1]-b[0]*a[1]
  print(top,bottom,top%bottom)
  #t0=(c[0]*b[1]-b[1]*c[2])/(a[1]*b[2]-b[1]*a[2])
  t0=Fraction(top,bottom)
  t1=Fraction(a[0]*c[1]-c[0]*a[1],a[0]*b[1]-b[0]*a[1])
  print(t0,t1)
  for i in range(3):
    print(a[i]*t0+b[i]*t1,c[i])
    assert a[i]*t0+b[i]*t1==c[i]
  #assert 
  print(t0)
  rp=tuple(s0[0][i]+t0*(s0[1][i]-rv[i]) for i in range(3))
  print(rp)
  return sum(rp)

print(part2(txt))