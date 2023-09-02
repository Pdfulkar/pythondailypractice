#StudentMarksReportEx1.py
#validation of Student Number
while(True):
   sno=int(input("Enter Student Number(100-200):"))
   if(sno>=100) and (sno<=200):
      break
   print("\t{} is Invalid Student Number-try agian".format(sno))
#accept name
sname=input("Enter Student Name")
#validation of Student Marks in C-100
while(True):
    cm=int(input("Enter Marks in C:"))
    if(cm>=0) and (cm<=100):
        break
    print("\t{} Invalid Marks in C Lang".format(cm))
#validation of Student Marks in C++-100
while(True):
    cppm=int(input("Enter Marks in C++:"))
    if(cppm>=0) and (cppm<=100):
        break
    print("\t{} Invalid Marks in C++ Lang".format(cppm))
#validation of Student Marks in Python-100
while(True):
    pym=int(input("Enter Marks in Python:"))
    if(pym>=0) and (pym<=100):
        break
    print("\t{} Invalid Marks in Python Lang".format(pym))
#Calculate Total Marks and percent of all 3 subjects
totmarks=cm+cppm+pym
percent=round((totmarks/300)*100,2)
#Decide the grade
if(cm<40) or    (cppm<40)  or  (pym<40):
    grade="FAIL"
else:
    if(250<=totmarks<=300):
        grade="DISTINCTION"
    elif(200<=totmarks<=249):
        grade="FIRTST"
    elif(150<=totmarks<=199):
        grade="SECOND"
    elif(120<=totmarks<=149):
        grade="THIRD"
#display Student Marks Report
print("="*50)
print("\tSTUDENT MARKS REPORT ")
print("="*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(sname))
print("\tStudent Marks in C Lang:{}".format(cm))
print("\tStudent Marks in C++ Lang:{}".format(cppm))
print("\tStudent Marks in PYthon Lang:{}".format(pym))
print("-"*50)
print("\tSTUDENT TOTAL MARKS:{}".format(totmarks))
print("\tSTUDENT PERCENTAGE OF MARKS:{}".format(percent))
print("\tSTUDENT RESULT:{}".format(grade))
print("="*50)
