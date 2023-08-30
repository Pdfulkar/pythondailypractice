#ForLoopEx4.py
n=int(input("Enter the range for generating Even Numbers:"))
if(n<=0):
    print("{} is Invalid".format(n) )
else:
    print("===========================")
    print("Even Numbers within:{}".format(n))
    print("===========================")
    for i in range(2,n+1,2):
        print("\t{} ".format(i))
    else:
        print("==============================")