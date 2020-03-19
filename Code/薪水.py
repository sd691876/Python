money=0
selary=0
while(True):
    selary=5000*0.08+5000*0.1+(money-10000)*0.12
    if(25000<selary):
        print("The sales amount $",money)
        print("is need to make a commission of $",300000//12)
        break
    else:
        money=money+3