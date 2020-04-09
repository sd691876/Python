import time,math
def distance(latitude1,longitude1,latitude2,longitude2):
    radius       = 6371.01
    distance     = radius*math.acos(math.sin(math.radians(latitude1)) * math.sin(math.radians(latitude2)) +    \
                                    math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) *    \
                                    math.cos(math.radians(longitude1-longitude2)))
    return distance
def area(d1,d2,d3):
    s=(d1+d2+d3)/2
    area         = math.sqrt(s*(s-d1)*(s-d2)*(s-d3))
    return area

#Problem2
latitude1, longitude1 = eval(input("Enter point 1(latitude and longitude) in degrees:"))
latitude2, longitude2 = eval(input("Enter point 2(latitude and longitude) in degrees:"))
print("The distance between the two points is ",distance(latitude1,longitude1,latitude2,longitude2),"km")

#Problem3
Charlotte   = (35.2270,-80.8431)
Sacannah    = (32.0835,-81.0998)
Orlando     = (28.5336,-81.3867)
Atlanta     = (33.7569,-84.3903)
d_CS        = distance(Charlotte[0],Charlotte[1],Sacannah[0],Sacannah[1])
d_SO        = distance(Sacannah[0],Sacannah[1],Orlando[0],Orlando[1])
d_CO        = distance(Charlotte[0],Charlotte[1],Orlando[0],Orlando[1])
d_CA        = distance(Charlotte[0],Charlotte[1],Atlanta[0],Atlanta[1])
d_AO        = distance(Atlanta[0],Atlanta[1],Orlando[0],Orlando[1])
d_AS        = distance(Atlanta[0],Atlanta[1],Sacannah[0],Sacannah[1])
print("The area is ",area(d_CS,d_CO,d_SO)+area(d_CO,d_CA,d_AO)," square kilometers") #118037.679680956
#print("The area is ",area(d_AO,d_SO,d_AS)+area(d_CS,d_CA,d_AS)," square kilometers") #118104.77137628873
'''
#Problem7
for i in range(0,2):
    print("The random uppercase letter according time.time() is: ",chr(int(time.time()*1000%26)+65))
'''
#Problem8
money=eval(input("Enter an amount as integer:"))
print("Your amount ",money," consists of\n",format(str(money//50)+" fifty dollars\n",'>20s'),format(str((money%50)//10)+" ten dollars\n",'>18s'),format(str((money%10)//5)+" five dollars\n",'>19s'),format(str(money%5)+" one dollars\n",'>18s'))
'''
#Problem11
num=input("Enter an integer: ")
print("The reversed number is: ",end="")
if(num[0]=='-'):
    print(num[0],end="")
    for i in range(len(num)-1,0,-1):
        print(num[i],end="")
else:
    for i in range(len(num)-1,-1,-1):
        print(num[i],end="")
'''

