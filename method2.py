# coding: utf-8
import numpy as np

def updtpdsum(data):
  pdsum = [0,0,0,0,0,0,0,0]
  for i in data:
    for j in range(8):
      pdsum[j] += i[j]

  pdmax=0
 


def total(data):
    sum = 0
    for i in data:
         for j in range(8):
             sum += i[j]
    return sum


def select(pdmax,data,people,ans):
    weight = [0]*16
    sum = 0
    for i in range(16):
      sum += data[i][pdmax]
    for i in range(16):
      weight[i] = data[i][pdmax]/sum
    a = np.random.choice(people, p=weight)
    ans[pdmax*2][1] = a
    weight2 = [i for i in weight if i != 0]
    if len(weight2) != 1:
        b = a
        while a == b:
            b = np.random.choice(people, p=weight)
        ans[pdmax*2+1][1] = b
        data[b-1] = [0]*8
        people[b-1] = 0
    data[a-1] = [0]*8
    people[a-1] = 0
    for i in range(16):
        data[i][pdmax] = 0

def fill(ans,people):
       if people != [0]*16:
            np.random.shuffle(people)
            people = [i for i in people if i != 0]
            print(people)
            print(ans)
            a = 0
            for i in ans:
                if i[1] == 0:
                    i[1] = people[a]
                    a += 1

def main():
    np.random.seed(0)
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
    people = [i for i in range(1,17)]
    #people = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
    while total(data) != 0:
        pdmax = updtpdsum(data)
        select(pdmax,data,people,ans)
    fill(ans,people)
    print(ans)

if __name__ == '__main__':
    main()
