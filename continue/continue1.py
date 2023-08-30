#Program for demonstrating Continute Statement
#ContinueEx1.py
s="PYTHON"
print("By using For Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("i am from for-else loop")
print("-----------------------------")
#My Requirement is To disp "PYTON"
for ch in s:
    if(ch=="H"):
        continue
    print("\t{}".format(ch))
else:
    print("i am from for-else loop")