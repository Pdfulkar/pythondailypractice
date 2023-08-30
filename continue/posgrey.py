#PosNegElementsSumEx.py
#Program for accepting Number of Numerical values and find sum of +ve and -ve numbers separately.
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
        ps,ns=0,0
        psl,nsl=[],[]  # Empty list
        for val in lst:
            if(val>0):
                psl.append(val)
                ps=ps+val
            elif(val<0):
                nsl.append(val)
                ns=ns+val
        else:
            print("Possitive Elements Sum({})={}".format(psl,ps))
            print("Negative Elements Sum({})={}".format(nsl,ns))