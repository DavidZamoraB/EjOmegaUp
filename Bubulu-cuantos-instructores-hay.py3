def largo_while(lista):
  largo = 0
  while lista != []:
    largo += 1
    lista = lista[1:]
  return largo

lista = list(map(str, input().split()))
print(largo_while(lista))