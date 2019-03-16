# madabikom a >= b
a = 12
b = 8
r = a%b

while(r != 0):
    a = b
    b = r
    r = a%b

print("pgcd = ", b)
uuu