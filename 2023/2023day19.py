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

result = 0

def isAccepted(vars,name="in"):
  #return True
  if name=="R":
    return False
  if name=="A":
    return True
  p=process[name]
  for op in p['ops']:
    val=vars[op['var']]
    if op['comp']=='>':
      passed=val>op['num']
    else:
      passed=val<op['num']
    if passed:
      return isAccepted(vars,op['res'])
  return isAccepted(vars,p['default'])

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
  
  
for part in parts:
  #print(part)
  rawvars=part[1:-1].split(",")
  vars={}
  for var in rawvars:
    name,num=var.split("=")
    num=int(num)
    vars[name]=num
  if isAccepted(vars):
    result+=sum(vars[key] for key in vars)

print(result)
