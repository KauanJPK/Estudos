
n = int(input("Insira um numero e direi se o mesmo é divisivel por 3 e 5"))
t = n % 3
c = n % 5
if t | c == 0:
    print("O numero é divisível por três e por cinco")
else:
    print(f"Numero indivisível por três e cinco, restos respctivos de cada:{t:.2f} e {c:.2f}")

