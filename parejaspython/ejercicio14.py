
for num in range(100, 1000):  
    
    c = num // 100
    d = (num // 10) % 10
    u = num % 10
    cubo = u**3 + d**3 + c**3 
    if cubo == num:
        print(num)