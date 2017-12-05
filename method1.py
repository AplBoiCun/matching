# coding: utf-8
import random

#はさみ、貯金箱、便座シート、コロコロ、Ziploc、ステッカー(猫)、Xmasカチューシャ、メダル
data = [
[0,0,0,2,3,0,0,0],
[0,2,0,0,3,0,0,0],
[0,0,0,0,0,0,0,0],
[0,5,0,0,0,0,0,0],
[0,0,0,5,0,0,0,0],
[0,0,0,5,0,0,0,0],
[0,2,0,0,3,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,3,2,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,5,0,0,0,0],
[0,0,0,2,3,0,0,0],
[0,3,0,0,0,2,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,5,0,0],
[0,0,0,2,3,0,0,0],
]

ans = [ [1,0],[1,0],[2,0],[2,0],[3,0],[3,0],[4,0],[4,0],[5,0],[5,0],[6,0],[6,0],[7,0],[7,0],[8,0],[8,0] ]
name = [i for i in range(16)]

    
def find(data):
  pdsum = [0,0,0,0,0,0,0,0]
  for i in data:
    for j in range(8):
      pdsum[j] += i[j]
    
  pdmax=0
  for i in range(8):
    if pdsum[pdmax]<pdsum[i]:
      pdmax=i
  return pdmax
       

def select(pdmax):  
  weight = [0]*16
  sum = 0
  for i in range(16):
     sum += data[i][pdmax]
  for i in range(16):
     weight = data[i][pdmax]/sum
        
  a = random.choice(name, p=weight) 
  ans[pdmax*2][1] = a
  data[a] = [0]*8

  total = 0
  for i in data:
        for j in range(8):
            total += i[j]
  
  if total != 0:  
      b = a
      while a == b:
        b = random.choice(name, p=weight) 
      ans[pdmax*2+1][1] = b
      data[b] = [0]*8



  
  
     
  
  



