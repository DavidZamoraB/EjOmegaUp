minutos = int(input())
pelis = int(input())
cont = 0
while pelis:
  mins = int(input())
  cont += mins
  pelis -=1
if cont<minutos:
  print("SI")
else:
  print("NO")