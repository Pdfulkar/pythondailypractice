#InnerLoopEx3.py--for loop in while loop
i=1
while(i<6): # Outer Loop
    print("-----------------------------")
    print("Value of i={}".format(i))
    print("-----------------------------")
    for j in range(3,0,-1): # Inner Loop
        print("\tValue of j={}".format(j))
    else:
        print("I am coming out of inner loop")
        i=i+1
else:
    print("I am coming out of outer loop")