C = float(input())
F = C * 1.8 + 32
K = C + 273.15
R = C * 9/5 + 491.67

if F == round(F):
  print(int(F))
else:
  print(round(F, 2))

if K == round(K):
  print(int(K))
else:
  print(round(K, 2))

if R == round(R):
  print(int(R))
else:
  print(round(R, 2))