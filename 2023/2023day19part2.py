from DataGetter import getData

year = 2023
day = 19

import re

txt="""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

txt=getData(year, day)

workflows,parts=[zone.split("\n") for zone in txt.split("\n\n")]

def splitVars(vars,name,middle):
  var=vars[name]
  if var[0]<middle and var[1]>=middle:
    smallout=dict(vars)
    bigout=dict(vars)
    smallout[name]=(var[0],middle-1)
    bigout[name]=(middle,var[1])
    return (smallout,bigout)
  if var[0]<middle:
    return (vars,None)
  if var[1]>=middle:
    return (None,vars)
  return (None,None)

def numPossible(vars,name="in"):
  print(name)
  if name=="R":
    return 0
  if name=="A":
    res=1
    for key in vars:
      res*=vars[key][1]-vars[key][0]+1
    return res
  p=process[name]
  print(p)
  res=0
  for op in p['ops']:
    print(op)
    name=op['var']
    num=op['num']
    val=vars[name]
    if op['comp']=='>':
      keep,test=splitVars(vars,name,num+1)
    else:
      test,keep=splitVars(vars,name,num)
    print(keep,test)
    if test is not None:
      res+=numPossible(test,op['res'])
    if keep is None:
      return res
    vars=keep
  return res+numPossible(vars,p['default'])

process={
  
}

for workflow in workflows:
  key,operations=workflow.split("{")
  operations=operations[:-1].split(",")
  ops=[]
  for operation in operations[:-1]:
    var,comp,num,res=re.match("([xmas])(<|>)(\\d*):(\\w*)",operation).groups()
    num=int(num)
    ops.append({
      'var':var,
      'comp':comp,
      'num':num,
      'res':res
    })
  process[key]={
    "ops":ops,
    "default":operations[-1]
  }
  
varNames="xmas"

result=numPossible({name:(1,4000) for name in varNames})

print(result)
