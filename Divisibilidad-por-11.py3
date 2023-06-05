N = int(input())
while N:
    Numer = int(input())
    if Numer % 11 == 0:
        print("El número " + str(Numer) + " es divisible por 11")
    else:
        print("El número " + str(Numer) + " no es divisible por 11")
    N-=1