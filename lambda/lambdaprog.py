#write a program for finding the larger program amond two
maximum = lambda a,b : a if a>b else b if b > a  else "Both are Equal"
ab = int(input("Put in second number"))
b = int(input("Put in second number"))
print("The bigger number is ",maximum(ab,b))