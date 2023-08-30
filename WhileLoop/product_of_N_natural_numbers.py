#program for Finding Product  of First N Natural Numbers
#NatNumsProductEx1.py
n = int(input("Put in the Number Here : "))
print("-" * 50)
print("Product of First {} Natural Numbers ".format(n))
print("-" * 50)
p,d=1,1
if (n<=0):
        print("The number are not natural number")
else:
    while(n>=d):
        p = p*d
        d += 1
print("-" * 50)
print(p)
print("-" * 50)