from DataGetter import getData

year = 2022
day = 12

txt=getData(year, day)

lines=txt.split("\n")

result = 0

for i, line in enumerate(lines):
  print(line)

print(result)
