#program for generating Mul table for a given number
#MulTableEx1.py
a = int(input("Put in the Number For the multiplication table : "))
print("=" * 50)
print("Mul Table for :{}".format(a))
print("=" * 50)
i=1
while(i<=10):
    print("\t {} * {} = {} ".format(a,i,a*i))
    i+=1
else:
        print("="*50)