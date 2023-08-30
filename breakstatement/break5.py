#Program for reading List of values and display
#ReadDispListvaluesEx1.py
n=int(input("Enter How Many Numbers u want to Enter:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=[] # OR lst=list()
    for i in range(1,n+1):
        val=int(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("="*40)
        print("Content of list=",lst)
        print("="*40)
