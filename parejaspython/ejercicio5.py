for num in range (1,1000 ):
    if num >1:
        for i in range (2, num):
            if (num%i)==0:
                print ("Numero: ",num)
                break
        else:
            print ("Numero primo: ",num)