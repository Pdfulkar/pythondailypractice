#Program for accepting Number of Numerical values and find sum of +ve and -ve numbers separately.
#ContinueEx3.py
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
        print("Content of list=",lst)#[10, -20, 30, -40, 25]
        print("="*40)
        #Code for finding Sum of +ve Numebrs
        ps=0
        for val in lst:
            if(val<0):
                continue
            print(val)
            ps=ps+val
        else:
            print("+Ve Elements Sum=",ps)
        # Code for finding Sum of -ve Numebrs
        ns=0
        for val in lst:
            if(val>0):
                continue
            print(val)
            ns=ns+val
        else:
            print("-Ve Elements Sum=",ns)