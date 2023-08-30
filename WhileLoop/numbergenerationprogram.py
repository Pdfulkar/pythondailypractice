#PROGRAM FOR GENERATING 1 TO N NUMBERS WHERE N IS +VE
#NumGenEx1.py
n=int(input("Enter How Many numbers u want to Generate:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("-" * 50)
    print("Numbers within:{}".format(n))
    print("-"*50)
    i=1 # Initlization Part
    while(i<=n): # Cond Part
        print("\t\t{}".format(i))
        i=i+1 # Updation Part
    else:
        print("=" * 50)
    print("i am from while--else part--other stmts ")
print("i am from if..else part--other stmts")