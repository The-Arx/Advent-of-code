from DataGetter import getData

year = 2023
day = 12

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

result = 0

for i, line in enumerate(lines):
  print(line)

print(result)
