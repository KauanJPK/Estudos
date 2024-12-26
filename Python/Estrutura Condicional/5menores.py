x1 = []
for a in range(4):
    x = int(input("Insira 4 números"))
    x1.append(x)
    x1.sort()
total = sum(x1[0:3])
print(total)