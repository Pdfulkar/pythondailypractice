
#ForLoopEx3.py
n=int(input("Enter a Number for generating Mul Table:"))
if(n<=0):
    print("{} is Invalid".format(n) )
else:
    print("===========================")
    print("Mul Table for {}".format(n))
    print("===========================")
    for i in range(1,11):
        print("\t{} x {}={}".format(n,i,n*i))
    else:
        print("==============================")
