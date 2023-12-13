from DataGetter import getData

year = 2023
day = 12

txt=getData(year, day)
#replace statments go here

lines=txt.split("\n")

result = 0

def setChar(string,i,char):
  return string[:i]+char+string[i+1:]
      
def possibleGroups(springs,groups):
  springs+="."
  cache=[[None]*len(groups) for _ in springs]
  def posGroupsHelp(i,j):
    if j>=len(groups):
      return 0 if "#" in springs[i:] else 1
    if i>=len(springs):
      return 0
    if cache[i][j] is not None:
      return cache[i][j]
    ans=0
    if i + groups[j] <= len(springs):
      if springs[i] in ".?":
        ans += posGroupsHelp(i+1,j)
  
      if springs[i] in "#?":
        if not "." in springs[i:i+groups[j]] and not "#"==springs[i+groups[j]]:
          ans+=posGroupsHelp(i+groups[j]+1,j+1)
    cache[i][j]=ans
    return ans
  
  return posGroupsHelp(0,0)

'''def possibleGroups(springs,groups,myGroups=None,i=0,group=0):
  if myGroups is None:
    myGroups=[]
  for j in range(i,len(springs)):
    char=springs[j]
    if char=="?":
      
      return possibleGroups(setChar(springs,j,"#"),groups,list(myGroups),j,group)+possibleGroups(setChar(springs,j,"."),groups,list(myGroups),j,group)
    elif char=="#":
      group+=1
    else:
      if group>0:
        #print(j,char,myGroups)
        myGroups.append(group)
        #print(myGroups,groups[:len(myGroups)])
        if myGroups!=groups[:len(myGroups)]:
          return 0
        group=0
  if group>0:
    myGroups.append(group)
    group=0
  #print(myGroups,groups)
  if myGroups==groups:
    return 1
  else:
    return 0'''

'''def possibleGroups(springs,groups):
  if "?" in springs:
    i=springs.index("?")
    return possibleGroups(setChar(springs,i,"#"),groups)+possibleGroups(setChar(springs,i,"."),groups)
  else:
    myGroups=[]
    group=0
    '''
for line in lines:
  #print(line)
  springs,groups=line.split(" ")
  newsprings=springs
  for i in range(4):
    newsprings+="?"+springs
  groups=list(map(int,groups.split(",")))
  newgroups=groups*5
  #print(springs)
  #print(groups)
  result+=possibleGroups(newsprings,newgroups)
  #print(result)
print(result)