def computeTax(status, taxableIncome):
    if(status==1):
        computeTax=((taxableIncome-33951)*0.25+(33950-8351)*0.15+8350*0.1)
    elif(status==2):
        computeTax=((taxableIncome-16701)*0.15+16700*0.1)
    elif(status==3):
        computeTax=((taxableIncome-33951)*0.25+(33950-8351)*0.15+8350*0.1)
    elif(status==4):
        computeTax=((taxableIncome-45501)*0.25+(45500-11951)*0.15+11950*0.1)
    return computeTax

print("taxable Income     Single     Married Joint     Married Separate     Head of a House")
for i in range(50000,60001,50):
    print(i,"      %d     %d     %d     %d"%(computeTax(1,i),computeTax(2,i),computeTax(3,i),computeTax(4,i)))