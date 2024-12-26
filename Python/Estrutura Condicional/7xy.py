x = int(input("Insira um número X e de acordo com o algoritimo lhe direi o Y"))
if x < 1:
    print(f"O Y é igual ao x, ou seja {x}")
elif x > 1:
    y = x * x
    print(f"O Y do seu algoritimo é:{y}")
elif x == 1:
    print('O seu Y é 0')