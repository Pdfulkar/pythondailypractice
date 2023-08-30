#program for Finding Product  of First N Natural Numbers
#Factorial
n = int(input("Put in the Number whose factorial you want : "))
p,d=1,1
if (n<=0):
        print("The factorial cannot be found")
else:
    while(n>=d):
        p = p*d
        d += 1
print("-" * 50)
print("Factorial of ",n," is ",p)
print("-" * 50)