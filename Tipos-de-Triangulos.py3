A,B,C = map(int, input().split())

igual = (A==B) and (B==C)

if igual:
  print("equilatero")
else:
  if A!=B and B!=C:
    print("escaleno")
  else:
    print("isosceles")