# coding: utf-8
import random

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
name = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16]
pdsum = [0,0,0,0,0,0,0,0]

for i in people:
  for j in range(8):
    pdsum[j] += i[j]

print(pdsum)

pdsum_sorted = pdsum.reverse()

for i in pdsum_sorted:
  a,b = select(pdsum.index(i))
  
def select(num):
  
  weight = [0]*16
  sum = 0
  for i in range(16):
     sum += people[i][num]
  for i in range(16):
     weight = people[i][num]/sum
  a = random.choice(name, p=weight) 
  b = random.choice(name, p=weight) 
  while a == b:
    b = random.choice(name, p=weight) 
  
  
  
     
  
  



