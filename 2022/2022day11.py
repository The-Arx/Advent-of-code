from DataGetter import getData

year = 2022
day = 11

txt="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

#txt=getData(year, day)
#replace statments go here

monkeys=[monkey.split("\n") for monkey in txt.split("\n\n")]

for i,monkey in enumerate(monkeys):
  monkeys[i]={
    "n":i,
    "items":list(map(int,monkey[1].split("  Starting items: ")[1].split(", "))),
    "operation":monkey[2].split("  Operation: new = old ")[1].split(" "),
    "test":int(monkey[3].split("  Test: divisible by ")[1]),
    "true":int(monkey[4].split("    If true: throw to monkey ")[1]),
    "false":int(monkey[5].split("    If false: throw to monkey ")[1]),
    "inspected":0,
  }
result = 0

def getVal(num,item):
  if num=='old':
    return item
  return int(num)

for i in range(20):
  for monkey in monkeys:
    for item in monkey['items']:
      op,num=monkey['operation']
      num=getVal(num,item)
      if op=="*":
        item*=num
      elif op=="+":
        item+=num
      item//=3
      if item%monkey['test']==0:
        nextmonkey=monkey['true']
      else:
        nextmonkey=monkey['true']
      monkeys[nextmonkey]['items'].append(item)
      monkey["inspected"]+=1
    monkey['items'].clear()
    

print(result)