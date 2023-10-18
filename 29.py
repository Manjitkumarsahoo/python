def fib():
	print("enter no of term ")
	r=int(input())
	a=0
	b=1
	print(a,b,end=" ")
	while r>2:
		c=a+b
		print(c,end=" ")
		a=b
		b=c
		r=r-1
fib()	