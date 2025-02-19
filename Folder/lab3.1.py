def kal(n):
	jal=0
	if(n==0):
		return 0
	else:
		return n%10 + kal(n//10)

n=int(input("enter the number"))
print(kal(n))
