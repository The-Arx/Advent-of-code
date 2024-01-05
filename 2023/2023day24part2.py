from DataGetter import getData
import scipy.optimize
from matplotlib import pyplot as plt
import numpy as np

year = 2023
day = 24

txt='''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''

#txt=getData(year, day)

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

def part2(txt):
  stones=parseData(txt)
  
  for stone in stones:
    for vel in stone[1]:
      assert vel!=0
  s0=stones[0]
  s1=stones[1]
  s2=stones[2]
  global f
  def f(times):
    #print(times)
    t0,t1=times
    p0=tuple(s0[0][i]+s0[1][i]*t0 for i in range(3))
    p1=tuple(s1[0][i]+s1[1][i]*t1 for i in range(3))
    dr=tuple((p1[i]-p0[i])/(t1-t0) for i in range(3))
    r=(tuple(p0[i]-t0*dr[i] for i in range(3)),dr)
    #print(" ",r)
    #print(" ",t1-t0)
    t2=tuple((-r[0][i]+s2[0][i])/(r[1][i]-s2[1][i]) for i in range(3))
    #print(" ",t2)
    return t2[0]-t2[1],t2[1]-t2[2],t2[2]-t2[0]
    
  def cleanF(times):
    try:
      return f(times)
    except ZeroDivisionError:
      return np.nan,np.nan
  
  t0=np.arange(0,20,0.01)
  t1=np.arange(0,20,0.01)
  times=np.meshgrid(t0,t1)
  output=cleanF(times)
  #plt.figure(1)
  plt.clf()
  #plt.imshow(output[0])
  colors="rgb"
  for i in range(3):
    plt.contour(output[i],levels=[0],colors=colors[i],extent=(t0[0],t0[-1],t1[0],t1[-1]))
  #plt.clim(-10,10)
  #plt.colorbar()
  #plt.figure(2)
  #plt.clf()
  #plt.imshow(output[1])
  #plt.contour(output[1],levels=[0],colors="b",extent=(t0[0],t0[-1],t1[0],t1[-1]))
  #plt.clim(-10,10)
  #plt.colorbar()
  
  
  #t1,t2=scipy.optimize.fsolve(f,(4,2))
  #print(t1,t2)
  #print(f((t1,t2)))
  
  result = 0
  
  #minNum=7
  #maxNum=27
  '''
  for i, stone in enumerate(stones):
    print(stone)
    for j in range(i):
      stone2=stones[j]
      intersect,x,y=findIntersect(stone,stone2)
      if intersect and x>=minNum and y>=minNum and x<=maxNum and y<=maxNum:
        result+=1
  '''
  return result

print(part2(txt))