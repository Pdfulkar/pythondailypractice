#program for cal Factorial of a Number
#Example:  4! = 1 x 2 x 3 x 4
#FactorialEx1.py
#not with for loop
n=int(input("Enter a a Number for Cal Factorial:"))
if(n<0):
    print("{} Invalid Input".format(n))
else:
    f=1
    for i in range(1,n+1):
        f=f*i
    else:
        print("Factorial({})={}".format(n,f))

#program for obtaining Factors of a Given Numbers
#FactorsEx1.py
# n=int(input("Enter a Number for finding Factors:"))
# if(n<=0):
#     print("{} is Invalid Input".format(n))
# else:
#     for i in range(1,n+1):
#         if(n%i==0):
#             print("\t{}".format(i))