import time
currentTime=int(time.time())
currentSecond=currentTime%60
currentMinute=(currentTime//60)%60
currentHour=(currentTime//3600)%24
region=eval(input("Enter the time zone offset to GMT:"))
print("Current time is",currentHour+int(region),":",currentMinute,":",currentSecond)


money=eval(input("Enter monthly saving amount:"))
reg=0
for i in range(0,6):
    predict_money=((money+reg)*(1+0.00417))
    reg=predict_money
print("After the six month, the amount values is:",predict_money)


year=eval(input("Enter the number of years: "))
population=312032486
Total_time=(year*31556926)
print("The population in",year,"years is ",population+Total_time//7-Total_time//13+Total_time//45)
