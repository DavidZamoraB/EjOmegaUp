def ordenar(L):
    if(L == []): return L
    Men = []
    May = []
    for i in L[1:]:
        if i<L[0]: Men.append(i)
        else: May.append(i)
    return ordenar(Men)+[L[0]]+ordenar(May)

def difSim(A,B):
    A = ordenar(A)
    B = ordenar(B)
    ds = []
    while(A and B):
        if A[0]<B[0]:
            ds.append(A[0])
            A = A[1:]
        elif A[0] == B[0]:
            A=A[1:]
            B=B[1:]
        else:
            ds.append(B[0])
            B=B[1:]
    return ds+A+B

A1, A2, B1, B2 = map(int, input().split())

A = []
for i in range (A1, A2+1):
  A.append(i)

B = []
for i in range (B1, B2+1):
  B.append(i)

if len(difSim(A,B)) != len(A+B):
  print("1")
else:
  print("0")