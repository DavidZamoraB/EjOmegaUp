A = int(input())
lista = list(map(int, input().split()))
C = int(input())
salida = lista[C:]
for i in salida:
  print(i, end=" ")