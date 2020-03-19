star=int(input("please input the star's number : "))
time=star
for star in range(star,0,-1):
    for time in range(time,0,-1):
        print("*",end=' ')
        if(time==1):
            star=star-1
            time=star
            print("")
            continue