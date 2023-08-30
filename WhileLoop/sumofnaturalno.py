#program for Finding Sum of First N Natural Numbers
#NatNumsSumEx1.py
N = int(input("Put in the natural number till which you want sum : "))
A,S=1,0
if (N<=0):
    print("The given number is not a natural number ")
    exit("The Given Program is Completed")
else:
    print("=" * 60)
    print("Thee sum till {} natural number is as follows ".format(N))
    print("=" * 60)
    while(N>=A):
        S=S+A
        A+=1
print("The Sum of natural numbers till {} is {}".format(N,S))
print("The Given Program is Completed")

