#Program for demonstrating Continute Statement
#ContinueEx2.py
s="PYTHON"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("i am from while-else loop")
print("-----------------------------")
#My Requirement is To disp "PYON"
i=0
while(i<len(s)):
    if(s[i]=="H") or (s[i]=="T"):
        i=i+1
        continue
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("i am from while-else loop")