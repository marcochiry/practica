res= 0
vector1 = []
for i in range(5):
    vector1.append(int(input("ingrese un numero")))

for i in range(5):
    res += vector1[i]
print (f"la suma total es : {res} ")