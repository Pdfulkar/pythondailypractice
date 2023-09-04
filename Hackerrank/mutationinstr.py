def mutate_string(string, position, character):
    p= []
    for ij in range(len(s)):
        p.append(*s[ij])
    p.pop(int(i))
    p.insert(int(i), c)
    s_new = "".join(p)
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)