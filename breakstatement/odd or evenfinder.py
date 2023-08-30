#Program for accepting a number and decides whether the given number is prime or not.
#PrimeEx2.py
n=int(input("Enter Any Number:"))
if(n<=1):
    print("{} is Invalid Number".format(n))
else:
    res=False
    for i in range(2,n):
        if(n%i==0):
            res=True
            break
    if(res):
        print("{} is Not Prime".format(n))
    else:
        print("{} is Prime".format(n))
