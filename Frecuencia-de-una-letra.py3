palabra, letra = map(str, input().split())
cont = 0
for l in list(palabra):
  if l == letra:
    cont +=1
print(cont)