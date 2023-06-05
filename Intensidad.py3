Q,C = map(str, input().split())
I, A = map(str, input().split())
res = float(Q)/float(I)

if res == round(res):
  print(round(res), "A")
else:
  print(res, "A")