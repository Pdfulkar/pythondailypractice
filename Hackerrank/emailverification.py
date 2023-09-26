def fun(s):
    # return True if s is a valid email, else return False

    email = False
    S = s.split("@",1)
    s1 = S[-len(S)+1].split(".")
    s2=S[-len(S)].replace("-","").replace("_","")
    if s2.isalnum() == True:
        if s1[-len(s1)].isalnum() == True:
            if s1[len(s1)-1].isalpha() == True and len(s1[len(s1)-1]) <= 3:
                email = True
    print(s,S,s1,s1[len(s1)-1].isalpha(),s1[-len(s1)].isalnum(),s2.isalnum(),len(s1[len(s1)-1]))
    if email == True:
        return s


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)