from aocd import data as txt

lines=txt.split("\n")

count=0
location=50 # starts at 50
shifts=0

part2=True

#pt 2 is less than 6568

for line in lines:
  priorLoc=location
  #print(line)
  delta=int(line[1:])
  if line[0] == "L": location-=delta
  else: location+=delta
  
  # keep within [0,99]
  deltaShift=0
  while location > 99:
    location -= 100
    if part2 and location != 0 and priorLoc != 0:
        deltaShift += 1
  while location < 0:
    location += 100
    if part2 and location != 0 and priorLoc != 0:
        deltaShift += 1
  
  # check
  if location == 0: count+=1
  count+=deltaShift
  shifts+=deltaShift
  print("Line:{};Location:{};DeltaShift:{};Count:{};".format(line,location,deltaShift,count))
 

print(count)
print(shifts)