from DataGetter import getData

year = 2023 ##insert year
day = 12 ##insert day

txt=getData(year, day)

def parseData(txt):
  return txt.split("\n")

def part1(txt):
  lines=parseData(txt)
  
  result = 0
  
  for i, line in enumerate(lines):
    print(line)
  
  return result

print(part1(txt))