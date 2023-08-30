#program for obtaining Factors of a Given Numbers
#FactorsEx1.py
n = int(input("Put in the number to find factorial :"))
if (n<=0):
    print("This is not a acceptable number")
else:
    i=1
    for i in range(i,n+1):
        if (n%i==0):
            print(i)
print("Above are the factors of the number {}".format(n))

