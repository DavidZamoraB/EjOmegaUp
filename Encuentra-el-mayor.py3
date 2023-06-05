N = int(input())
lista = list(map(int, input().split()))
mayor = 0
for i in lista:
  if i>mayor:
    mayor = i
print(mayor)