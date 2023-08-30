#big of three number
a = float(input("Put in the Number :"))
b = float(input("Put in the Number :"))
c = float(input("Put in the Number :"))
if ((a>=b) and (a>c)):
    print("BIG({} {} {} is {})".format(a,b,c,a))

elif ((b>=a) and (b>c)):
    print("BIG({} {} {} is {})".format(a,b,c,b))


elif ((c>=b) and (c>a)):
    print("BIG({} {} {} is {})".format(a,b,c,c))

else:
    print("The Values are Equal")