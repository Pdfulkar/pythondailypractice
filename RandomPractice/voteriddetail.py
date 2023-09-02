#VoterEx2.py
while(True):
    age=int(input("Enter Age of Citizen:"))
    if(age>=18) and (age<=100):
        break
    print("\t{} is Invalid Age--try again".format(age))
print("{} Years Citizen is Eligible to Vote:".format(age))
