F = int(input())
NueveC = (F-32)*5
C = NueveC//9
FoC = 0
if C>36:
  FoC = 1

print(str(C) + " " + str(FoC))