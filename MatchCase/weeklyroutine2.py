#MatchCaseEx4.py
wkd=input("Enter week name:")
match(wkd.upper()):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print("{} is Working Day:".format(wkd))
    case "SATURDAY":
        print("{} is Week End---UGA:".format(wkd))
    case "SUNDAY":
        print("{} is HoliDay".format(wkd))
    case _:
        print("{} is not a week day".format(wkd))