from DataGetter import getData

year = 2023
day = 6

txt=getData(year, day)
#replace statments go here
txt=txt.replace(" ","")
time,dist=[int(line.split(":")[1]) for line in txt.split("\n")]

result = 0


for j in range(time):
  if j*(time-j)>dist:
    result+=1
    

print(result)