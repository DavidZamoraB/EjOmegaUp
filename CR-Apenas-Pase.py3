PrAmigos = float(input())
T = int(input())
total = 0
cont = 0
while T:
    A = float(input())
    total += A
    cont +=1
    T -= 1
PrGil = total/cont


if PrGil>PrAmigos:
  print("Presume")
else:
  print("Ladra")