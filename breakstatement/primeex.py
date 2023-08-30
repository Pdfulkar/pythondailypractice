#Program for accepting a number and decides whether the given number is prime or not.
#PrimeEx1.py
n=int(input("Enter Any Number:"))
if(n<=1):
    print("{} is Invalid Number".format(n))
else:
    res="Prime"
    for i in range(2,n):
        if(n%i==0):
            res="Not Prime"
            break

    if(res=="Prime"):
        print("{} is {}".format(n,res))
    else:
        print("{} is {}".format(n, res))