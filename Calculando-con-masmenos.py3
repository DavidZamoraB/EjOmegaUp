A, B, C, = map(float, input().split())
if B == 0:
    print("indefinido")
else:
    mas = (A / B) + C
    menos = (A / B) - C
    if mas == menos:
        print("{:.6f}".format(mas))
    else:
        print("{:.6f} ".format(mas) + "{:.6f}".format(menos))