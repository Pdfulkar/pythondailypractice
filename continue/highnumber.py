#program for finding sum of digits of Numbers of list
#ListNumbersDigitsSumEx1.py
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
        print("Content of list=",lst)#[123,456,12,45]
        print("="*40)
        sumlist=[]
        s=0
        for val in lst:
            for d in str(val):
                s=s+int(d)
                sumlist.append(s)
        else:
            print("Given List={}".format(lst))
            print("Sum List={}".format(sumlist))

