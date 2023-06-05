T = int(input())
n = int(input())
cont = 0
while T:
  a = int(input())
  if a == n:
      cont +=1
  T -= 1
print(cont)