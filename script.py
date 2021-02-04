import pinyin

import json

import os 

from termcolor import colored

try:
  os.mkdir("input")
  os.mkdir("output")
  
except:
  
  def conversor():
    
    print(colored("Conversor Of Ktape Chinese To Pinyin","red") + "\n")
    
    print(colored("Compatible With (WII,PS3 & Xbox360)","green"))
    
    KtapeDir = os.listdir("input")
  
    with open("input//" + KtapeDir[0]) as jsonfile:
      Ktape = json.load(jsonfile)
      
    i = 0 
    _Clips = []
    _class = '{"__class":"Tape","Clips":'
    
    while i < len(Ktape["Clips"]):
      Clips = Ktape["Clips"][i]
      i = i + 1
      
      Clips["Lyrics"] = pinyin.get(Clips["Lyrics"],format="strip")
      
      _Clips.append(Clips)
      
    with open("output//" + KtapeDir[0],"w") as g:
      g.write(_class)
      g.write(json.dumps(_Clips))
      g.write("}")
    
    
  
  conversor()
  
  
  
  
  
      
    