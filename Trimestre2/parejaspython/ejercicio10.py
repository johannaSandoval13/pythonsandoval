def mcd (a,b):
    while a % b != 0:
        r= a % b
        a = b
        b = r
    return b

print (mcd (60, 80))
