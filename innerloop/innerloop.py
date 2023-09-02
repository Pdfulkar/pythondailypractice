#InnerLoopEx1.py--for loop in for loop
for i in range(1,6):
    print("-----------------------------")
    print("Value of i={}".format(i))
    print("-----------------------------")
    for j in range(1,4):
        print("\tValue of j={}".format(j))
    else:
        print("I am coming out of inner loop")
else:
    print("I am coming out of outer loop")