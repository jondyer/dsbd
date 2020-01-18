lst = [1,2,3,4,5,6,7,8,9,10]


def oddeven():
    odd=0
    even=0
    for x in lst:
        if x%2==0:
            even+=x*x
        else:
            odd += x*x
    return ('odd', odd), ('even', even)

print( oddeven() )