def Palindrome(digit):
    [hun,ten,unit]= digit
    if(hun==unit):
        print("{:s} is a palindrome.".format(digit))
    else:
        print("{:s} is not a palindrome.".format(digit))
        
def Arithmetic_Geometric_Mean_Inequality(point):
    [x,y]= point
    max_x = 200
    max_y = 100
    if(0<=x*y<=(max_x/2)*(max_y/2) and 0<=x<=max_x and 0<=y<=max_y):
        print('The point is in the triangle')
    else:
        print('The point is not in the triangle')

def Base_transform(digit):
    if(type(digit)==str):
        if(65<=ord(digit)<=70):
            print('The decimal value is ',ord(digit)-55)
        else:
            print('The decimal value is ', digit)
    else:
        base =16
        digit %= base
        if( digit%base > 9):
            digit = chr(digit+55)
        print('The hexadecimal value is ', digit)
        

#Problem 26
digit = input("Enter a three digit integer: ")
while(len(digit)!=3):
    coefficient = input("Enter a three digit integer: ")    
Palindrome(digit)

#Problem 27
point = [float(num) for num in input("Enter a point's x and y coordinates: ").split(",")]
while(len(point)!=2):
    point = [float(num) for num in input("Enter a point's x and y coordinates: ").split(",")]
Arithmetic_Geometric_Mean_Inequality(point)

#Problem 33
digit = eval(input("Enter a decimal value(0 to 15): "))
if(0<=digit<=15):
    Base_transform(digit)
else:
    print('Invalid input')
'''
#Problem 34
character = input('Enter a hexadecima character: ')
while(len(character)!=1):
    character = input('Enter a hexadecima character: ')
if(48<=ord(character)<=57 or 65<=ord(character)<=70):
    Base_transform(character)
else:
    print('Invalid input')
'''
