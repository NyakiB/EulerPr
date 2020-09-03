def n_factor(n):
    import operator,functools
    return functools.reduce(operator.mul,(item for item in range(1,n+1)),1)

def sum_digits(n):
    return sum((int(i) for i in str(n)))

    
print(sum_digits(n_factor(100)))
