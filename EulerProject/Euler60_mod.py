import itertools
def is_prime_two(num1, num2):
    # type: (object, object) -> object
    numcon1 = int(str(num1)+str(num2))
    if is_prime(numcon1):
        numcon2 = int(str(num2)+str(num1))
        if is_prime(numcon2):
            return True
    return False


def is_prime(num):
    val = True
    if num == 1:
        return False
    if num == 2:
        return True
    if num%2 == 0:
        return False
    for x in range(3,int(num**0.5)+1,2):
        if num%x == 0:
            val = False
            break
    return val

prime_list_long = []
for x in range(1,10000):
    if is_prime(x):
        prime_list_long.append(x)
print prime_list_long
print len(prime_list_long)

prime_list = prime_list_long

pairs =[]
for i in prime_list:
    for j in reversed(prime_list):
        if i<j:
            if is_prime_two(i, j):
                pairs.append([i,j])
        else:
            break
print pairs
            # for indk, k in enumerate(nplj):
            #     nplk = nplj[indk+1:]
#                 # print i,j,k
#                 if is_prime_two(i,k) and is_prime_two(k,i):
#                     if is_prime_two(k,j) and is_prime_two(j,k):
#                         for indl, l in enumerate(nplk):
#                             npll = nplk[indl+1:]
#                             if is_prime_two(i,l) and is_prime_two(l, i):
#                                 if is_prime_two(l, j) and is_prime_two(j, l):
#                                     if is_prime_two(l, k) and is_prime_two(k,l):
#                                         for m in npll:
#                                             if is_prime_two(m, i) and is_prime_two(i, m):
#                                                 if is_prime_two(m,j) and is_prime_two(j,m):
#                                                     if is_prime_two(m, k) and is_prime_two(k, m):
#                                                         if is_prime_two(m,l) and is_prime_two(l,m):
#                                                             print i,j,k,l,m
#                                                             print i+j+k+l+m
#                                                             break
#
#
#
#
