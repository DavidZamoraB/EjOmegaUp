C = int(input())
lista = []
while C != 1:
  if C%2==0:
    C = C//2
    lista.append(C)
  else:
    C = C*3+1
    lista.append(C)
lista.append(C)

def largo_for(n):
  largo = 0
  for elemento in n:
    largo += 1
  return largo

print(largo_for(lista))