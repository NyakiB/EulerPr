def lattice_paths(x,y):
    x+=1
    y+=1
    from functools import reduce
    return reduce(lambda x, y: x * y, [a for a in range(1,x+y-2)], 1)//(reduce(lambda x, y: x * y, [a for a in range(1,x-1)], 1)*reduce(lambda x, y: x * y, [a for a in range(1,y-1)], 1))

print(lattice_paths(20,20))

