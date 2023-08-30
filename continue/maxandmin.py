#Program for finding Max and Min from list of Elements without using max() and min()
#MaxMinElementsEx1.py
n=int(input("Enter How Many Values u want to Enter:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=[] # OR lst=list()
    for i in range(1,n+1):
        val=int(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("="*40)
        print("Content of list=",lst)# [10, 23, -4, 34, 12]
        print("="*40)
        if(len(set(lst))==1):
            print("All values are equal")
        else:
            #Code Max and Min
            maxv,minv=lst[0],lst[0]
            for val in lst:
                if(val>maxv):
                    maxv=val
                elif(val<minv):
                    minv=val
            else:
                print("Max({})={}".format(lst,maxv))
                print("Min({})={}".format(lst, minv))

