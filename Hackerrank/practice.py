def count_substring(string, sub_string):
    start = 0
    count = 0
    while start<len(string):
        index = string.find(sub_string,start)
        if (index == -1):
            break
        count+=1
        start = index+1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)