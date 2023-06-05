T = int(input())

lista = list(map(int, input().split()))
par_o_impar = int(input())
for i in lista:
  if (par_o_impar == 0):
    if(i%2==0): print(i, end=" ")
        
  else:
    if(i%2==1): print(i, end=" ")