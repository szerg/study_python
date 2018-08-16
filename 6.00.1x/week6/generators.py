def genNumber():
    import math
    number=2
    while True:
        prime = True
        for i in range(2,int(math.sqrt(number)+1)):
            if number%i == 0 and number != 2:
                prime = False
                break
        if prime:
            yield number
        number+=1

nr=genNumber()
print nr.next()
print nr.next()
    

