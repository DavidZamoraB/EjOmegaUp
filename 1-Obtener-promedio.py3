alum = int(input())
lista = list(map(int, input().split()))

def promedio_for(lista):
    suma = 0
    for elemento in lista:
        suma += elemento

    return suma / alum

print("{:.2f}".format(promedio_for(lista)))