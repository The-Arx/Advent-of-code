#!/usr/bin/env python3
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path
import re

path=Path(__file__).parent

templatePath=Path(path,"template.py")

def getPath(year,day):
  return Path(path,"{}/{}day{}.py".format(year,year,day))

def error(error,msg):
  RED = "\033[38;2;255;0;0m"
  NORMAL="\033[0m"
  print(RED+error+": "+NORMAL+msg)
  sys.exit(1)

def getInt(val,arg="argument"):
  try:
    return int(val)
  except ValueError:
    error("Invalid {}".format(arg),"{} is not an int".format(arg))
    
def reReplace(string,name,value):
  return re.sub("(^|\n)(\\s*{}\\s*=\\s*)\\d+\\s*##insert {}".format(name,name),"\\1\\g<2>{}".format(value),string)

def createFromTemplate(year,day):
  year=getInt(year,"year")
  day=getInt(day,"day")
  if day<1:
    error("Invalid day","day must be greater than or equal to one")
  if day>25:
    error("Invalid day","day must be less than or equal to twenty-five")
  if year<2015:
    error("Invalid year","AoC started in 2015")
  try:
    templateFile=templatePath.open()
  except FileNotFoundError:
    error("Template not found","Template not found in {}".format(templatePath))
  with templateFile as template:
    newFilePath=getPath(year,day)
    try:
      newFile=newFilePath.open("x")
    except FileExistsError:
      error("Already exsists","File {} already exists".format(newFilePath))
    with newFile as file:
      txt=template.read()
      txt=reReplace(txt,"day",day)
      txt=reReplace(txt,"year",year)
      file.write(txt)
      print("File created sucessful in {}".format(newFilePath))
  
#error("Error","This is a description")
  
args=sys.argv[1:]
if len(args)==0:
  time = datetime.now(ZoneInfo("EST")) + timedelta(hours=1)
elif len(args)==1:
  if len(args[0])<=2:
    pass
  elif len(args[0])==4:
    pass
  
elif len(args)==2:
  createFromTemplate(args[0], args[1])
else:
  error("Too many args","this program only takes 0 to 2 args")