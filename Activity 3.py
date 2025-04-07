def fac(x):
    '''Factorial calculator'''
    if x == 1 or x == 0:
        return 1
    else:
        return x*fac(x-1)

print (fac.__doc__)
print ("the factorial of 4:", fac(4))