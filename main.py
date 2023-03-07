from os import remove 
from os.path import exists
x=1
while True:
  x+=1
  print(x)
  y = str(x)
  if exists("./files/"+y+".txt"):
    remove("./files/"+y+".txt")     
  f=open("./files/"+y+".txt","w")
  f.write(y * 100000)
  f.close()
