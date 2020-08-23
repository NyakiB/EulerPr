lista,listb,listc=[],[],[]
searcha,searchsb,searchc=[],[],[]

def pythtrip(limit):
    c,m=0,2
    while c<limit:
        for n in range(1,m):
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            if c> limit:
                break
            lista.append(a)
            listb.append(b)
            listc.append(c)
        m=m+1

pythtrip(1001)
for countera, valuea in enumerate(listaa):
    for counterb, valueb in enumerate(listab):
        for counterc, valuec in enumerate(listac):
          if valuea+valueb+valuec==1000:
              if countera==counterb==counterc:
                  searcha.append(valuea)
                  searchb.append(valueb)
                  searchc.append(valuec)
summ=searcha[0]*searchb[0]*searchc[0]
print(summ)
