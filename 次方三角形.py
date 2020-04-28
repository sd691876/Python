def Power_Pyramid(integer):
    for i in range(1,integer+1):
        for j in range(integer-i,0,-1):
            print("    ", end = "")
        for k in range(-i,i+1):
            if(k != 0 and k != 1):
                print(format(abs(2)**(i-abs(k)),">4d"), end = "")
        print("")
            
while(1):
    integer = eval(input("Enter integer(1 to 15) to show the pyramid: "))
    Power_Pyramid(integer)
