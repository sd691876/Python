def ID(iid):
    Id = {"A":10, "B":11, "C":12, "I":34, "O":35, "D":13, "E":14 ,\
          "F":15, "G":16, "H":17, "J":18, "K":19, "L":20, "M":21 ,\
          "N":22, "P":23, "Q":24, "R":25, "S":26, "T":27, "U":28 ,\
          "V":29, "X":30, "Y":31, "W":32, "Z":33, "Z":33, "1": 1 ,\
          "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8 ,\
          "9": 9, "0": 0}
    weight = [1,9,8,7,6,5,4,3,2,1,1]
    summation = Id[iid[0]]//10
    for i in range(len(weight)-1):
        summation = summation + (Id[iid[i]]%10)*weight[i+1]
    print(summation)

iid = [num for num in input('ID: ')]
ID(iid)
