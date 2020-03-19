loan_amount=float (input("Loan Amount: "))
year=int (input("Number of year: "))
rate=float (input("Enter annual interest: "))
rate=rate*0.01
a=0
print("Interest Rate        Monthly Payment        Total Payment")
for i in range(0,25):
    print(end='   ')
    print("%5.2f"%(rate*100)+"%",end='                 ')
    a=loan_amount*(rate/12)/(1-(1/((1+rate/12)**(year*12))))
    print("%6.2f"%a,end='              ')
    print("%8.2f"%(a*year*12))
    rate=rate+0.00125