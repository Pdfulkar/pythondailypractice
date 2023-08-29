#program for accepting two numerical value and finding the big one and also if the number are same
#if____else as a operator project
a=float(input("Enter the First Number : "))
b=float(input("Enter the Second Number : "))
c= a if a>b else b if b>a else " Both valses are same"
print("big({},{})= {}".format(a,b,c))