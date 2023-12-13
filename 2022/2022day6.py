from DataGetter import getData

year=2022
day=6

txt=getData(year,day)
#replace statments go here




i = 0
sub = ""
while i < len(txt):
  char=txt[i]
  if char in sub:
    sub = sub[sub.index(char)+1:]
  sub+=char
  i += 1
  if len(sub) == 14:
    print(i)
    break

