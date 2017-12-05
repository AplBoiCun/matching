# coding: utf-8
import random

#はさみ、貯金箱、便座シート、コロコロ、Ziploc、ステッカー(猫)、Xmasカチューシャ、メダル
data = [
[0,0,0,0,1,0,4,0],
[0,0,2,2,1,0,0,0],
[0,0,0,0,5,0,0,0],
[0,0,0,3,0,2,0,0],
[0,0,0,0,0,5,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
]

people = [i for i in range(16)]
pdsum = [0,0,0,0,0,0,0,0]
ans = [[1,0],[1,0],[2,0],[2,0],[3,0],[3,0],[4,0],[4,0],[5,0],[5,0],[6,0],[6,0],[7,0],[7,0],[8,0],[8,0]]

for i in people:
  for j in range(8):
    pdsum[j] += i[j]

print(pdsum)

pdsum_sorted = pdsum.reverse()

for i in pdsum_sorted:
  a,b = select(pdsum.index(i))
 

def select(pdmax):  
  weight = [0]*16
  sum = 0
  for i in range(16):
     sum += data[i][num]
  for i in range(16):
     weight = data[i][num]/sum
  a = random.choice(people, p=weight) 
  ans[pdmax*2][1] = a
  data[a] = [0]*8
  b = random.choice(people, p=weight)
  ans[pdmax*2+1][1] = b
  data[b] = [0]*8
  while a == b:
    b = random.choice(people, p=weight) 
  data[a] = [0]*8
  data[b] = [0]*8
       
  ans[pdmax]

  
  
     
  
  



