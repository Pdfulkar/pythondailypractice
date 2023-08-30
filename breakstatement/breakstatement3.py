#program for Deciding whether the given number is Perfect or not
#Perfect Number:  Sum of the factors of Given Number is equal to original number
#PerfectNumberEx1.py
n=int(input("Enter a Number for finding Factors:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    s=0
    for i in range(1,(n//2)+1):
        if(n%i==0):
            print("\t{}".format(i))
            s=s+i
    else:
        if(s==n):
            print("{} is Perfect Number".format(n))
        else:
            print("{} is Not Perfect Number".format(n))