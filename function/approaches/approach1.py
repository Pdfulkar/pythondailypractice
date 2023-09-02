#Function for addition of Two Numbers
#Approach1.py
#Input: From Function Call
#Process: In Function Body
#Output: To Function Call
def sumop(a,b): # Function Def--a , b are called Formal params
    c=a+b # here c is called Local variable
    return c

#mainj program
x=float(input("Enter First value:"))
y=float(input("Enter Second value:"))
res=sumop(x,y) # Function Call
print("sum({},{})={}".format(x,y,res))


