#MatchCaseEx3.py
wkd=input("Enter week name:")
match(wkd):
    case "MONDAY" | "monday":
        print("""{} is Working Day:
You shoul study python notes from 11 am to 5pm and practice the question from hackerrank
also focus on your basic health""".format(wkd))

    case "TUESDAY" | "tuesday":
        print("""{} is Working Day:
You shoul study python notes from 11 am to 5pm and practice the question from hackerrank
also focus on your basic health""".format(wkd))

    case "WEDNESDAY" | "wenesday":
        print("""{} is Working Day:
You shoul study python notes from 11 am to 5pm and practice the question from hackerrank
also focus on your basic health""".format(wkd))

    case "THURSDAY" | "thursday":
        print("""{} is Working Day:
You shoul study python notes from 11 am to 5pm and practice the question from hackerrank
also focus on your basic health""".format(wkd))

    case "FRIDAY" | "friday":
        print("""{} is Working Day:
You shoul study python notes from 11 am to 5pm and practice the question from hackerrank
also focus on your basic health""".format(wkd))

    case "SATURDAY" | "saturday":
        print("""{} is Working Day:
You shoul study python notes from 11 am to 5pm and practice the question from hackerrank
also focus on your basic health""".format(wkd))

    case "SUNDAY" | "sunday":
        print("""{} is Holiday:
Enjoy but also focus on your basic health""".format(wkd))

    case _:
        print("{} is not a week day".format(wkd))