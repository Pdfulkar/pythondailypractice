#InnerLoopEx2.py--while loop in while loop
i=1
while(i<6): # Outer Loop
    print("-----------------------------")
    print("Value of i={}".format(i))
    print("-----------------------------")
    j=1
    while(j<4): # Inner Loop
        print("\tValue of j={}".format(j))
        j=j+1
    else:
        print("I am coming out of inner loop")
        i=i+1
else:
    print("I am coming out of outer loop")