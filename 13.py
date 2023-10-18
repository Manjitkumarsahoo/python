print("enter a number")
number=int(input())
temp1=number
temp=number
while temp!=1 and temp!=4:
    sum=rem=0
    while number>0:
        rem=number%10
        sum=sum+pow(rem,2)
        number=number//10
    temp=sum
    number=temp
if temp==1:
    print("\n%d is a happy number."%temp1)
else:
    print("\n%d is not a happy number"%temp1)
