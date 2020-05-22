import os
import sys
def Q1():
    keywords = {'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', \
                'class', 'continue', 'def', 'del','elif', 'else', 'except', 'finally',   \
                'for', 'from','global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',  \
                'not', 'or', 'pass','raise', 'return', 'try', 'while', 'with', 'yield'}
    filename = input("Enter a python source code filename: ").strip()                     
    if not os.path.isfile(filename):
        print("File", filename, "does not exits")
        sys.exit()
    infile = open(filename, "r")
    text = infile.read().split()    
    count = 0
    reg_word = []
    for word in text:
        if word in keywords :
            if word not in reg_word:
                reg_word.append(word)
                count += 1           
    print("The number of keywords in",filename, "is", count)
    print("The keywords are",set(reg_word))

def Q2():
    numbers = [int(num) for num in input("Enter the numbers: ").split(" ")]
    count = {}
    for i in range(len(numbers)):
        if str(numbers[i]) not in count:
            count["%d"%numbers[i]] = 1
        else:
            count["%d"%numbers[i]] += 1
    print("The numbers with the nost occurrence are: ")
    for key in count:
        if(count[key]==max(count.values())):
            print(key,end = " ")
    print("")
    
def Q3():
    filename = input ("Enter a Python source code filename: ").strip()
    if not os.path.isfile(filename):
        print("File", filename, "does not exits")
        sys.exit()
    infile = open(filename, "r")
    text = infile.read().split()
    keywords = {}
    for key in text:
        if key not in keywords:
            keywords[key] = 1
        else:
            keywords[key] += 1
    print(keywords)

def Q8():
    filename = input ("Enter a text filename: ").strip()
    if not os.path.isfile(filename):
        print("File", filename, "does not exits")
        sys.exit()
    infile = open(filename, "r", encoding='utf-8')
    text = infile.read().encode('utf-8').decode('utf-8-sig').split()
    reg_word = []
    for word in text:
        if word not in reg_word:
            reg_word.append(word)
    reg_word.sort()
    for word in reg_word:
        print(word,end=" ")
    print("")


#Problem 1
Q1()

#Problem 2
Q2()    
   
#Problem 3
Q3()                     

#Problem 8
Q8()
