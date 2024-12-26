print("CALCULADORA DE JUROS")

c = float(input("Insira o valor do seu capital:\n"))
i = float(input("Insira a porcentagem da sua taxa:\n"))
t = int(input("Insira o tempo:\n"))
j = (c * i * t)/100
print(f"O valor do seu juros é de {j}")