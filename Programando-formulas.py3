x,y,z = map(float, input().split())
solu = (x + x * (y + z**2)) / ((x + 3.14159265359) * (y + 3.14159265359))

print("{:.6f} ".format(solu))