import string
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
