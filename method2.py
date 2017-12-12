# coding: utf-8
import numpy as np
import copy

def updtpdsum(data):
    pdsum = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in data:
        for j in range(8):
            pdsum[j] += i[j]


def total(data):
    sum = 0
    for i in data:
        for j in range(8):
            sum += i[j]
    return sum


def change_data(data):
    data_edited = [[0]*8]*16
    for i in range(8):
        for j in range(8):
            if data[i][j] == "A":
                data_edited[i][j] = 100
            if data[i][j] == "B":
                data_edited[i][j] = 50
            if data[i][j] == "C":
                data_edited[i][j] = 10
            if data[i][j] == "D":
                data_edited[i][j] = 2
            if data[i][j] == "E":
                data_edited[i][j] = 1
    return data_edited

def select(pdmax, data, ans):
    people = [i for i in range(1, 17)]
    weight = [0] * 16
    sum = 0
    for i in range(16):
        sum += data[i][pdmax]
    for i in range(16):
        weight[i] = data[i][pdmax] / sum
    a = np.random.choice(people, p=weight)
    ans[pdmax * 2][1] = a
    weight2 = [i for i in weight if i != 0]
    if len(weight2) != 1:
        b = a
        while a == b:
            b = np.random.choice(people, p=weight)
        ans[pdmax * 2 + 1][1] = b
        data[b - 1] = [0] * 8
        people[b - 1] = 0
    data[a - 1] = [0] * 8
    people[a - 1] = 0
    for i in range(16):
        data[i][pdmax] = 0



def evaluate(data, ans, best_ans, best_evallist):
    evallist = [0,0,0,0,0] #A,B,C,D,Eの数
    for i in ans:
        if data[i[1]-1][i[0]-1] == "A":
            print("Checker6")
            evallist[0] += 1
        if data[i[1]-1][i[0]-1] == "B":
            evallist[1] += 1
        if data[i[1]-1][i[0]-1] == "C":
            evallist[2] += 1
        if data[i[1]-1][i[0]-1] == "D":
            evallist[3] += 1
        if data[i[1]-1][i[0]-1] == "E":
            evallist[4] += 1
    if (evallist[3]+evallist[4]) < (best_evallist[3] + best_evallist[4]) or \
    (((evallist[3]+evallist[4]) == (best_evallist[3] + best_evallist[4])) and ((evallist[0]+evallist[1]) > (best_evallist[0] + best_evallist[1]))) or \
    (((evallist[3]+evallist[4]) == (best_evallist[3] + best_evallist[4])) and ((evallist[0]+evallist[1]) == (best_evallist[0] + best_evallist[1])) and ((evallist[4]) < (best_evallist[4]))) or \
    (((evallist[3]+evallist[4]) == (best_evallist[3] + best_evallist[4])) and ((evallist[0]+evallist[1]) == (best_evallist[0] + best_evallist[1])) and ((evallist[4]) == (best_evallist[4])) and ((evallist[0]) > (best_evallist[0]))):
        best_ans = ans
        best_evallist = evallist
    return best_ans, best_evallist




def main():
    np.random.seed(0)
    # はさみ、貯金箱、便座シート、コロコロ、Ziploc、ステッカー(猫)、Xmasカチューシャ、メダル
    # Aは1番目に欲しいもの、Bは2番目に欲しいもの、Cは欲しくないけどキレないもの、Dは2番目にキレるもの、Eは1番目にキレるもの
    data = [
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "C", "B", "C", "C", "E", "D", "C"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["C", "B", "A", "C", "C", "D", "C", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"],
        ["A", "B", "C", "C", "C", "C", "D", "E"]
    ]

    ans = [[1, 0], [1, 0], [2, 0], [2, 0], [3, 0], [3, 0], [4, 0], [4, 0], [
        5, 0], [5, 0], [6, 0], [6, 0], [7, 0], [7, 0], [8, 0], [8, 0]]

    best_ans = [[1, 1], [1, 2], [2, 3], [2, 4], [3, 5], [3, 6], [4, 7], [4, 8], [
        5, 9], [5, 10], [6, 11], [6, 12], [7, 13], [7, 14], [8, 15], [8, 16]]
    best_evallist = [0,0,0,0,16]

    for i in range(10):
        data_edited = change_data(data)
        print(data_edited)
        pdlist = [0, 1, 2, 3, 4, 5, 6, 7]
        np.random.shuffle(pdlist)
        for k in range(8):
            updtpdsum(data_edited)
            pdmax = pdlist[k]
            select(pdmax, data_edited, ans)
        best_ans, best_evallist = evaluate(data, ans, best_ans, best_evallist)
        print(best_ans, best_evallist)



if __name__ == '__main__':
    main()
