# coding: utf-8
importt numpy as np

#はさみ、貯金箱、便座シート、コロコロ、Ziploc、ステッカー(猫)、Xmasカチューシャ、メダル
people = [
[0,0,0,0,1,0,4,0],
[0,0,2,2,1,0,0,0],
[0,0,0,0,5,0,0,0],
[0,0,0,3,0,2,0,0],
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
[0,0,0,0,0,0,0,0],
]

pdsum = [0,0,0,0,0,0,0,0]

for i in people:
  for j in range(8):
    pdsum[j] += i[j]

print(pdsum)

pdsum_sorted = pdsum.sorted()

for i in pdsum_sorted:
  a,b = select(pdsum.index(i))
  
def select(num):
  data = [0]*16
  sum = 0
  for i in range(16):
     sum += people[i][num]
  for i in range(16):
     data = people[i][num]/sum
  
  
  
  
     
  
  



