#program for accepting a number and decding whether the given number is even or odd
#EvenOddEx1.py
while(True):
    a = int(input("enter the value : "))
    if (a % 2 == 0 and a != 0):
        print("The given Number is Even Number")
    elif(a==0):
        print("Cannot Determine SoRRy !! :)")
    else:
        print("The given Number is Odd Number")
