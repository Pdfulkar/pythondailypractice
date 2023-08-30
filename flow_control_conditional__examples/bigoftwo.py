
#Program for accepting Two numerical Integer values and find biggest among them cnad check for equality
#BigTwoEx2.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
if(a>b):
    print("Big({},{})={}".format(a,b,a))
if(b>a):
    print("Big({},{})={}".format(a,b,b))
if(a==b):
    print("Both the values are equal:")