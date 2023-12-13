from DataGetter import getData

year = 2023
day = 7

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

hands=[]

for line in lines:
  hand,bet=line.split(" ")
  hands.append({
    'hand':hand,
    'bet':int(bet)
  })



strengths=["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def setChar(string,i,c):
  return string[:i]+c+string[i+1:]

def subscore(hand):
  if "J" in hand:
    jindex=hand.index("J")
    best=6
    for char in strengths:
      if char=="J":
        continue
      best=min(best,subscore(setChar(hand,jindex,char)))
    return best
  symbols=[{"c":card,"num":hand.count(card)} for card in strengths]
  symbols.sort(key=lambda d:d['num'], reverse=True)
  bnum=symbols[0]['num']
  if bnum==5:
    return 0
  if bnum==4:
    return 1
  if bnum==3 and symbols[1]['num']==2:
    return 2
  if bnum==3:
    return 3
  if bnum==2 and symbols[1]['num']==2:
    return 4
  if bnum==2:
    return 5
  return 6

def score(handobj):
  hand=handobj['hand']
  score=subscore(hand)
  for char in hand:
    score*=len(strengths)
    score+=strengths.index(char)
  return score

hands.sort(key=score)

result = 0

for i, hand in enumerate(hands):
  result+=hand['bet']*(len(hands)-i)
  print(i,hand,hand['bet']*len(hands)-i,len(hands)-i,result)

print(result)