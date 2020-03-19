year=int(input("Enter a year: "))
firstDay=int(input("Enter the first day of the year: "))
month=1
day=1
if(firstDay==7):
    firstDay=0
if(year%4==0):
    allDay=366
for i in range(0,12):
    if(month==1):
        print("     January  ",year)
    elif(month==2):
        print("     February  ",year)   
    elif(month==3):
        print("     March  ",year)  
    elif(month==4):
        print("     April  ",year)  
    elif(month==5):
        print("     May  ",year)  
    elif(month==6):
        print("     June  ",year)  
    elif(month==7):
        print("     July  ",year)  
    elif(month==8):
        print("     August  ",year)  
    elif(month==9):
        print("     September  ",year)  
    elif(month==10):
        print("     October  ",year)  
    elif(month==11):
        print("     November  ",year)  
    elif(month==12):
        print("     December  ",year)
    print("\nSun Mon Tue Wed Thu Fri Sat")           
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        print(" ",end=' ')
        for j in range(0,firstDay*4):               
            print(end=' ')
        for k in range(0,31):
            if(day<10):    
                print(day,end='   ')
            else:    
                print(day,end='  ')
            day+=1
            firstDay+=1
            if(firstDay==7):
                print("\n")
                print(end=' ')
                firstDay=0
    elif(month==4 or month==6 or month==9 or month==11):
        print(" ",end=' ')
        for j in range(0,firstDay*4):               
            print(end=' ')
        for k in range(0,30):
            if(day<10):    
                print(day,end='   ')
            else:    
                print(day,end='  ')
            day+=1
            firstDay+=1
            if(firstDay==7):
                print("\n")
                print(end=' ')
                firstDay=0 
    elif(month==2 and year%4==0):
        print(" ",end=' ')
        for j in range(0,firstDay*4):               
            print(end=' ')
        for k in range(0,29):
            if(day<10):    
                print(day,end='   ')
            else:    
                print(day,end='  ')
            day+=1
            firstDay+=1
            if(firstDay==7):
                print("\n")
                print(end=' ')
                firstDay=0 
    elif(month==2 and year%4!=0):
        print(" ",end=' ')
        for j in range(0,firstDay*4):               
            print(end=' ')
        for k in range(0,28):
            if(day<10):    
                print(day,end='   ')
            else:    
                print(day,end='  ')
            day+=1
            firstDay+=1
            if(firstDay==7):
                 print("\n")
                 print(end=' ')
                 firstDay=0
    print("\n\n")
    month+=1
    day=1