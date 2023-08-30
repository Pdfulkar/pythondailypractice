#Program for finding Highest Word Length
#HighestWordLengthEx1.py
n=int(input("Enter How Many Words u want to Enter:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    lst=[] # OR lst=list()
    for i in range(1,n+1):
        val=input("Enter {} Word:".format(i))
        lst.append(val)
    else:
        print("="*40)
        print("Content of list=",lst)#['python', 'liril', 'java', 'mom', 'teacher']
        print("="*40)
        dobj={}
        for word in lst:
            dobj[word]=len(word)
        else:
            for wn,wl in dobj.items():
                print("\t{}\t{}".format(wn,wl))
            else:
                #Coding for obtaining Max Length Word(s)
                maxlen=[]
                mv=max(dobj.values())
                for word,wlen in dobj.items():
                    if(wlen==mv):
                        maxlen.append(word)
                else:
                    print("Max Length Word(s)")
                    for word in maxlen:
                        print("\t{}".format(word))