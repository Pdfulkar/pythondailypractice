#program for cal Factorial of a Number
#Example:  4! = 4 x 3 x 2 x 1
#FactorialEx2.py
n = int(input("Put in the number :"))
if(n<=0):
    print("The number is not accepatable")
else:
    a,i=1,1
    for i in range (1,n+1,1):
        a=a*i
    print("{} is the factorial of number {}".format(a,n))
