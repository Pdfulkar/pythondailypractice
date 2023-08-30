#MatchCaseEx1.py
import sys
print("="*50)
print("\tArithmetic Operations")
print("="*50)
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Division")
print("\t6.Exponentiation")
print("\t7.Exit")
print("="*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1:
        print("Enter Two Values for addition:")
        a,b=int(input()),int(input())
        print("sum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Substraction:")
        a, b = int(input()), int(input())
        print("sub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two Values for Multiplication:")
        a, b = int(input()), int(input())
        print("mul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Values for Division:")
        a, b = int(input()), int(input())
        print("N.Div({},{})={}".format(a, b, a / b))
        print("F.Div({},{})={}".format(a, b, a // b))
    case 5:
        print("Enter Two Values for Modulo Division:")
        a, b = int(input()), int(input())
        print("Mod.Div({},{})={}".format(a, b, a % b))
    case 6 :
        a, b = int(input("Enter Base:")), int(input("Enter Power:"))
        print("Power({},{})={}".format(a, b, a** b))
    case 7:
        print("Thx for using program")
        sys.exit()
    case _:
        print("Ur Selection of Operation wrong-try again")

print("Program execution Completed")