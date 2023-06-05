N = int(input())
lista = list(map(int, input().split()))
cont = 0
for i in lista:
  if i%2==0:
    cont = 1
    print("[" + str(i) + "]", end=" ")
if not(cont):
  print(":(")