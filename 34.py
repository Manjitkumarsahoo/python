#Local and Global variabole

amount=10000
def deposite(amt):
    global amount
    amount=amount+amt
    print(amt,"deposite")
def withdraw(amt):
    global amount
    amount=amount-amt
    print(amt,"withdraw ")
print("balance=",amount)
deposite(3000)
withdraw(6000)
print("balance=",amount)
