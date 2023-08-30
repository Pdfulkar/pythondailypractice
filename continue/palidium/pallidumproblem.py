#PalindromeWordsEx1.py
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
        #Code for obtaining Palindrome words
        plist=[]
        for word in lst:
            if(word==word[::-1]):
                plist.append(word)
        else:
            print("List of Palindromes={}".format(plist))


