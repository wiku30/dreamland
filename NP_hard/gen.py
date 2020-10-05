import random

id = input();

id_bytes = bytes(id, "ascii")
bits = ''.join(["{0:08b}".format(x) for x in id_bytes])

n = len(bits)

N = 1000

print(n)
print(N)


def get_lit(i):
    return (i+1) * (2*int(bits[i])-1)

for t in range(N):
    i = random.randint(0,n-1)
    p = random.randint(0,2)
    true_lit = get_lit(i)
    for j in range(3):
        if j == p:
            print(true_lit)
        else:
            tmp = random.randint(0,n-1)
            rand_true = get_lit(tmp)
            if random.randint(0,3)==0:
                print(rand_true)
            else:
                print(-rand_true)
