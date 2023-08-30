#program for obtaining Factors of a Given Numbers
#FactorsEx2.py
import time
n=int(input("Enter a Number for finding Factors:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    for i in range(1,(n//2)+1):
        if(n%i==0):
            print("\t{}".format(i))
    else:
        print("\t{}".format(n))