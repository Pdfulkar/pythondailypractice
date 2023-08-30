#MatchCaseEx4.py
wkd=input("Enter week name:")
if wkd.upper() in ["MONDAY","TUESDAY","WEDNESDAY","FRIDAY","THURSDAY","SATURDAY","SUNDAY","MON","TUE","WED","THU","FRI","SAT","SUN"]:
    match(wkd[:3].upper()):
        case "MON"|"TUE"|"WED"|"THU"|"FRI":
            print("{} is Working Day:".format(wkd))
        case "SAT":
            print("{} is Week End---UGA:".format(wkd))
        case "SUN":
            print("{} is HoliDay".format(wkd))
else:
    print("{} is not a Week Day".format(wkd))
