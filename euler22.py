f=open(r'C:\Users\Bálesz\Desktop\names.txt',"r")
names=sorted([item for sublist in [x.replace('"','').split(",") for x in f] for item in sublist])
f.close()
abc={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
     'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
     'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
sub=[]
for counter,value in enumerate(names):
    pr=0
    for i in value:
        pr+=abc.get(i)
    pr*=(counter+1)
    sub.append(pr)
print(sum(sub))

