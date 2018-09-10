# pset2 problem 1
balance=0
annualInterestRate=0.0
monthlyPaymentRate=0.0 # minimum monthly payment rate
# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Test Case 2:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def rb(balance, annualInterestRate, monthlyPaymentRate): # remaining balance
    prevBalance = balance
    # required math
    # Monthly interest rate= (Annual interest rate) / 12.0
    mir = (annualInterestRate)/12.0
    # Minimum monthly payment = (Minimum monthly payment rate) x    (Previous balance)
    mmp = (monthlyPaymentRate)*prevBalance
    # Monthly unpaid balance = (Previous balance) - (Minimum monthly    payment)
    mub = prevBalance - mmp
    # Updated balance each month = (Monthly unpaid balance) + (Monthly  interest rate x Monthly unpaid balance)
    ubem = mub + mir * mub
    rb = ubem
    return rb # return remaining balance

#  Month 1 Remaining balance: 40.99
# m1rb = rb(balance, annualInterestRate, monthlyPaymentRate)
# print("%.2f" % m1rb)
# m2rb = rb(m1rb, annualInterestRate, monthlyPaymentRate)
# print("%.2f" % m2rb)

# balance after one year
def b1y(balance,annualInterestRate,monthlyPaymentRate):
    m = 1 # month
    mrb = 0.0
    while(m <= 12):
        if(m == 1):
            mrb = rb(balance,annualInterestRate,monthlyPaymentRate)  
        if( m > 1 and m <= 12 ):
            # monthly remaining balance
            mrb = rb(mrb,annualInterestRate,monthlyPaymentRate)
        # print mrb
        m += 1
        # print m    
    return mrb

b1yv = b1y(balance,annualInterestRate,monthlyPaymentRate)
print("%.2f" % b1yv)     

# Result Your Code Should Generate Below:
# Remaining balance: 31.38
          
# To make sure you are doing calculation correctly, this the 
# remaining balance you should be getting at each month fthis example
#  Month 1 Remaining balance: 40.99
#  Month 2 Remaining balance: 40.01
#  Month 3 Remaining balance: 39.05
#  Month 4 Remaining balance: 38.11
#  Month 5 Remaining balance: 37.2
#  Month 6 Remaining balance: 36.3
#  Month 7 Remaining balance: 35.43
#  Month 8 Remaining balance: 34.58
#  Month 9 Remaining balance: 33.75
#  Month 10 Remaining balance: 32.94
#  Month 11 Remaining balance: 32.15
#  Month 12 Remaining balance: 31.38