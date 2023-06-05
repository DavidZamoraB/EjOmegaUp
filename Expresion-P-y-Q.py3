P, Q = map(int, input().split())

def elevar(a,n):
  if n==0:
    return 1
  r = elevar(a, n>>1)
  r*=r
  if n%2:
    r*=a
  return r

operacion = (elevar(P,3)) + (elevar(Q,4)) - (2*(elevar(P,2)))

if operacion < 680:
  print(P)
  print(Q)
else:
  print()