e = int(input())

L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

for i in range (e):
  print(L1[i]+L2[i], end=" ")