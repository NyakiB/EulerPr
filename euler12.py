import math

def nth_triangle_num(n):
    """The function returns the nth triangle number."""
    return((n*(n+1))/2)

def divisor_gen(n):
    """The function returns the divisors of a number. It uses the quadratic sieve algorithm."""
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            yield i
            if i is not n/i:
                divisors.insert(0,n/i)
    for div in divisors:
        yield div

def divisors(n):
    return([d for d in divisors_gen(n)])

def search(n):
    """The functions return the triangle number for which divisors exceed the inputed number."""
    div,i=0,1
    while div<n:
        i+=1
        num=nth_triangle_num(i)
        div=len(divisors(num))
    return(num)

print(search(500))
    
    
