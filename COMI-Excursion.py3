n, p = map(int, input().split())
estu = []
while n:
  Al = int(input())
  estu.append(Al)
  n -=1

while p:
  preg = int(input())
  print(estu[preg-1])
  p-=1