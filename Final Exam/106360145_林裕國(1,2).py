import string

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
    if(summation%10==0):
        print('Id. number {} is valid.'.format(''.join(iid)))
    else:
        print('Id. number {} is invalid.'.format(''.join(iid)))

def readtxt(f):
    file = open(f, 'r')
    line = file.read()
    file.close()
    
    return line

def words(txt):
    txt = txt.replace('\n', '')
    for c in string.punctuation:
        txt = txt.replace(c, ' ')
    words = txt.split(' ')
    return words

def f(words):
    f_dic = {}

    for w in words:
        if w in f_dic:
            f_dic[w] += 1
        else:
            f_dic[w] = 1
    return f_dic
    
def sim(f1, f2):
    diff = 0
    
    for w in f1.keys():
        if w in f2.keys():
            diff += abs(f1[w] - f2[w])
        else:
            diff += f1[w]
    for w in f2.keys():
        if w not in f1.keys():
            diff += f2[w]
    total = sum(f1.values()) + sum(f2.values())
    diff = diff / total
    sim = 1.0 - diff
    return round(sim, 2)

#Problem 2
txt1 = readtxt('sonnet18.txt')
txt2 = readtxt('sonnet19.txt')
words1 = words(txt1)
words2 = words(txt2)
f1 = f(words1)
f2 = f(words2)

print('Sonnet18 與 Sonnet19 相似度 : ',sim(f1, f2))

txt1 = readtxt('sonnet18.txt')
txt2 = readtxt('sonnet18_r1.txt')
words1 = words(txt1)
words2 = words(txt2)
f1 = f(words1)
f2 = f(words2)

print('Sonnet18修改前後相似度 : ',sim(f1, f2))


#Problem 2
iid = [num for num in input('Please Enter your ID No.: ')]
ID(iid)
