number_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
nmbr_list=["one","two","three","four","five","six","seven","eight","nine"]
teen_list = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
decades_list =["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def no_of_digits(n):
    return len([item for item in str(n)])

def number_digit_to_words(n):
    import math
    if n <= 9:
        return(number_list[n])
    elif n >= 10 and n <= 19:
        tens = n%10
        return(teen_list[tens])
    elif n > 19 and n <= 99:
        ones = math.floor(n/10)
        twos = ones - 2
        tens = n % 10
        if tens == 0:
            return(decades_list[twos])
        elif tens != 0:
            return(decades_list[twos] + "-" + number_list[tens])
    elif n>99 and n<1000:
        tens=number_digit_to_words(int("".join(([item for item in str(n)][-2:]))))
        hund=nmbr_list[int([item for item in str(n)][0])-1]
        if n%100==0:
            return (hund+" hundred")
        else:
            return (hund+' hundred and '+tens)
    elif n==1000:
        return ('one thousand')
    else:
        raise ValueError('{0} is over the maximum.'.format(n))

def generate_words(n):
    list_for_result=[]
    for i in range(1,n+1):
        list_for_result.append(number_digit_to_words(i))
    return list_for_result

def sum_words(n):
    count=0
    for i in n:
        count+=len(i.replace(" ","").replace("-",""))
    return count

print(sum_words(generate_words(1000)))
