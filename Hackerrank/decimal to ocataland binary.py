def print_formatted(number):
    # your code goes here
    for i in range(number+1):
        print("\t{}\t{}\t{}\t{}" .format(i,oct(i),hex(i),bin(i)))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)