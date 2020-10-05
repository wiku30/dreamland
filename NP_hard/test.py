import random

print("Enter ID:")

id = input()

id_bytes = bytes(id, "ascii")
bits = ''.join(["{0:08b}".format(x) for x in id_bytes])

def check(lit):
    p = abs(lit)-1
    if (bits[p]=='1') & (lit > 0):
        return 1
    if (bits[p]=='0') & (lit < 0):
        return 1
    return 0 

with open('3sat.txt') as f:
    n = int(f.readline())
    N = int(f.readline())
    if len(bits)!= n:
        print('Wrong!')
    else:
        wrong = 0
        lit = [0,0,0]
        for t in range(N):
            tmp = 0
            for k in range(3):
                lit[k] = int(f.readline());
                if check(lit[k]) == 1:
                    tmp += 1
            if tmp == 0:
                print('Wrong!')
                wrong = 1
                break
        if wrong == 0:
            print('Correct!')
