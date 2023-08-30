#Program for reading List of words and find their length
#WordsLength.py
n=int(input("Enter How Many Words u want to Enter:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        word=input("Enter {} Word:".format(i))
        lst.append(word)
    else:
        d={} # Create an empty dict object
        for word in lst:
            d[word]=len(word)
        else:
            print("=====================")
            print("WordName\tlength")
            print("=====================")
            for wn,wl in d.items():
                print("\t{}\t{}".format(wn,wl))
            else:
                print("=====================")
