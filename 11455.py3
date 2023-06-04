A = int(input())
B = list(map(int, input().split()))
T = int(input())


for i in B:
  if i%T==0:
    print(i,end=" ")
  else:
    print("X",end=" ")