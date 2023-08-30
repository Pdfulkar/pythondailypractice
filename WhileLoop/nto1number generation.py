#PROGRAM FOR GENERATING N  to 1 NUMBERS WHERE N IS +VE
#NumGenEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    print("="*50)
    print("Number from {} to 1".format(n))
    i=n # Initlization Part
    while(i>=1): # Condition Part
        print("\t\t{}".format(i))
        i=i-1 # Updation Part
    else:
        print("="*50)