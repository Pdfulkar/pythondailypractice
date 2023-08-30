#Program for accepting a number and find its digits sum
#DigitsEx1.py
n=int(input("Enter a Number:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    s=0
    for d in str(n):
        v=int(d)
        s=s+v
    else:
        print("Digits Sum({})={}".format(n,s))
