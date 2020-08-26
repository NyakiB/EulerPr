import math

def artm_seq(start_num, diff, end_num):
    seq=[]
    for i in range(start_num**2, end_num+1, diff):
        seq.append(i)
    return sor

def sieves(n):
    primes=[]
    bool_list=[False]+[True for i in range(n-1)]
    for i in range(int(math.sqrt(n)+1)):
                      if bool_list[i]==True:
                          non_prime_index=artm_seq(i+1, i+1, n)
                          for j in non_prime_index:
                              bool_list[j-1]=False
    for i in range(n):
        if bool_list[i]==True:
                      primes.append(i+1)
    return primes

print(sum(sieves(2000000)))
