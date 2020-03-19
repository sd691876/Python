def futurelInvestmentValue(investmentAmount, monthlyInterestRate, years):
    futurelInvestmentValue = investmentAmount*((1+monthlyInterestRate*0.01)**(years*12))
    print("%6.2f"%futurelInvestmentValue)
    
investmentAmount=int(input("Enter investment amount: "))
monthlyInterestRate=int(input("Enter yearly interest rate: "))/12
print("Years     Future Value")
for i in range(1,31):
    print("%2d"%i,"      ",end=' ')
    futurelInvestmentValue(investmentAmount, monthlyInterestRate, i)