letra = (input())
T = int(input())

while T:
  pal = list(map(str, input()))
  if pal[0] == letra:
    for i in pal:
      print(i,end="")
  T-=1