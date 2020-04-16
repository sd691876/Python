def Study_loans(money):
    year =10
    total_year = 4
    summation = money
    for i in range(2,year+2):
        money = money * (1 + 0.05)
        print("The {:d} year cost is: {:.1f}".format(i, money))
        if(i <= total_year):
            summation = summation + money
    print("Total cost of study loans during {:d} years: {:.1f}" \
          .format(total_year, summation))
        
def Find_Pole(students):
    name     = []
    score    = []
    for i in range(students):
        name.append(input("Enter a student name: "))
        score.append(eval(input("Enter a student score: ")))
    score_len = len(score)
    sort_score = sorted(score)
    print("Top two students: ")
    for i in range(2):
        position = score.index(sort_score[score_len-(i+1)])
        print("{:s}'s score is: {:d}".format(name[position], score[position]))

def Pyramid(integer):
    for i in range(integer,0,-1):            #digit column
        for j in range(i):                  #space
            print("   ", end = "")
        for k in range(-(integer-i+1), (integer-i+1)+1):
            if(k != 0 and k != 1):
                print(format(abs(k),">3d"), end = "")
        print("\n")

def Triangle(integer):
    print("Pattern A\n")
    for i in range(integer,0,-1):
        for j in range(0,integer-i+1):
            print(format(j+1, ">3d"), end = "")
        print("\n")
        
    print("Pattern B\n")
    for i in range(integer,0,-1):
        for j in range(1,i+1):
            print(format(j, ">3d"), end = "")
        print("\n")
        
    print("Pattern C\n")
    for i in range(integer,0,-1):
        for j in range(1,i):
            print("   ", end = "")
        for k in range(integer-i+1,0,-1):
            print(format(k, ">3d"), end = "")
        print("\n")
        
    print("Pattern D\n")
    for i in range(integer,0,-1):
        for j in range(0,integer-i):
            print("   ", end = "")
        for k in range(i):
            print(format(k+1,">3d"), end = "")
        print("\n")
'''                
#Problem 9
money = 10000
Study_loans(money)

#Problem 11
students = eval(input("Enter the number of students: "))
Find_Pole(students)
'''
#Problem 19
integer = eval(input("Enter integer(1 to 15) to show the pyramid: "))
Pyramid(integer) 
'''
#Problem 20
integer = eval(input('Please enter a positive integer:  '))
Triangle(integer)
'''
