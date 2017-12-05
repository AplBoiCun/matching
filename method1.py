# coding: utf-8
import random
    
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

def total(data):
    sum = 0
    for i in data:	
         for j in range(8):		
             sum += i[j]	
    return sum
 

def select(pdmax,data):  		 
    weight = [0]*16		   
    sum = 0		  
    for i in range(16):		   
      sum += data[i][pdmax]		
    for i in range(16):		  
      weight = data[i][pdmax]/sum		
         		
    a = random.choice(name, p=weight) 		
   ans[pdmax*2][1] = a		
   data[a] = [0]*8		 
   people.remove(a)	
 		
   if total(data) != 0:  		
       b = a		
       while a == b:		
         b = random.choice(name, p=weight) 		
       ans[pdmax*2+1][1] = b		
       data[b] = [0]*8		
       people.remove(b)		
     		
 for i in range(16):		
     data[i][pdmax] = 0		
  

def fill(ans,people):
       if people != []:
            random.shuffle(people)
            for i in ans:
                if i[1] == 0:
                i[1] = people[0]
                people.remove(people[0])
                
def main():
    #はさみ、貯金箱、便座シート、コロコロ、Ziploc、ステッカー(猫)、Xmasカチューシャ、メダル
    data = [
    [0,0,0,0,1,0,4,0],
    [0,0,2,2,1,0,0,0],
    [0,0,0,0,5,0,0,0],
    [0,0,0,3,0,2,0,0],
    [0,0,0,0,0,5,0,0],
    [4,1,0,0,0,0,0,0],
    [0,0,0,2,0,0,1,2],
    [0,0,0,0,0,2,0,3],
    [0,0,0,0,0,0,5,0],
    [0,4,0,1,0,0,0,0],
    [5,0,0,0,0,0,0,0],
    [0,0,3,2,0,0,0,0],
    [0,0,5,0,0,0,0,0],
    [1,0,0,0,4,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ]
    ans = [ [1,0],[1,0],[2,0],[2,0],[3,0],[3,0],[4,0],[4,0],[5,0],[5,0],[6,0],[6,0],[7,0],[7,0],[8,0],[8,0] ]
    people = [i for i in range(16)]
    
    while total(data) != 0:
        pdmax = find(data)
        select(pdmax)
    fill(ans,people)
    print(ans)

    
    if __name__ == '__main__':
    main()
    
                    
  
     
  
  



