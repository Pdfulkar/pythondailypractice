#program for accepting Line of Text and print and count number of vowels
#NumberVowels.py
text=input("Enter Line of Text:") #Apple is in Red
nov=0
for ch in text:
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        print("\t{}".format(ch))
        nov=nov+1
else:
    print("Number of Vowels={}".format(nov))
