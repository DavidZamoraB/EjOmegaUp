def fibo(n):
  return fiboaux(0,1,n)

def fiboaux(p,u,n):
  if(n): return fiboaux(u, u+p, n-1)
  return p
  
N = int(input())
cont = 1
while cont<N+1:
  print(fibo(cont), end=" ")
  cont +=1