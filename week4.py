
def quan_tic():
    tic="QAN.AX"
    print(tic)
    return tic
res=quan_tic()
print(res)

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

print(qan_tic)

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

tic = "WES.AX"            # (5)
print(tic)                # (6)
qan_tic()

def qan_tic():            # (1)
    print(tic)            # (3)
    return tic            # (4)

qan_tic()                 # (7)
tic = "WES.AX"            # (5)
print(tic)

test_list=[0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]

def is_even_num(lis):
    evennum=[]
    for n in lis:
        if n % 2==0:
            evennum.append(n)
    print(evennum)
    return evennum
is_even_num(test_list)

lst=[2,3,10,14,20,21,25,13,15]
evens=[x**2 for x in lst if x**2>150]
print(evens)

numbers=[0,1,1,2,5,6,8,2,4,6,8]
new_num={x for x in numbers if x%2==0}
print (new_num)
