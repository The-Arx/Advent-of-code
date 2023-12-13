import requests
import sys
from pathlib import Path

path=Path(__file__)
dataPath=Path(path.parent,"data")

def getPath(year,day):
  return Path(dataPath,"{}day{}.txt".format(year,day))

def getData(year,day):
  try:
    file=getPath(year,day).open()
  except FileNotFoundError:
    return fetchData(year,day)
  else:
    txt=file.read()
    file.close()
    return txt
    
def fetchData(year, day, saveToFile=True ,session=None):
  url="https://adventofcode.com/{}/day/{}/input".format(year,day)
  if(session==None):
    try:
      file=path.with_name("session.txt").open()
    except FileNotFoundError:
      return fetchNewSession(year,day)
    else:
      session=file.read()
      file.close()
  headers = {
    'User-Agent': 'jonathan.gassend@gmail.com'
  }
  cookies = {
    "session" : session
  }
  r = requests.get(url, cookies = cookies, headers=headers)
  if(r.status_code!=200):
    print(r)
    print(r.text)
    if r.status_code==404:
      print("Data has not been released yet")
      sys.exit()
      #raise ProblemFetchException("Data has not been released yet")
    if r.status_code==500:
      return fetchNewSession(year,day)
    raise ProblemFetchException("Status code {}: \"{}\"".format(r.status_code,r.text))
  txt = r.text
  if txt[-1]=="\n":
    txt=txt[:-1]
  if saveToFile:
    dataPath.mkdir(exist_ok=True)
    with getPath(year,day).open("w") as file:
        file.write(txt)
  return txt
  
def fetchNewSession(year, day, message="New session required"):
  session=input(message+": (leave blank to cancel)\n").strip()
  if session=="":
    print("Data fetch canceled")
    sys.exit()
  with path.with_name("session.txt").open("w") as file:
    file.write(session)
  return fetchData(year,day,session=session)

class ProblemFetchException(Exception):
    pass