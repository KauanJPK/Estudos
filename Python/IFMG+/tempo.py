print("CONVERSOR DE TEMPO\n")

print('Lista de conversões:\n1- Minutos > Horas\n2- Horas > Minutos\n3- Segundos > Minutos\n4- Minutos > Segundos')
op = int(input("Insira a opção pela qual você quer converter:\n"))

if op == 1:
    print("Ótimo, você escolheu a opção que converte minutos em horas\nAgora insira a baixo o valor em minutos que você gostaria de converter:\n")
    min = int(input(""))
    horas = min/60
    print(f"Seu tempo em horas é de {horas}")

elif op == 2:
    horas = int(input("Ótimo, você escolheu a opção que converte horas em minutos\nAgora insira a baixo o valor em minutos que você gostaria de converter:\n"))
    min = horas * 60
    print(f"Seu tempo em minutos é de {min}")

elif op == 3:
    seg = int(input("Ótimo, você escolheu a opção que converte segundos em minutos\nAgora insira a baixo o valor em minutos que você gostaria de converter:\n"))
    min = seg / 60
    print(f"Seu valor em minutos é de {min}")

elif op == 4:
    min = int(input("Ótimo, você escolheu a opção que converte minutos em segundos\nAgora insira a baixo o valor em minutos que você gostaria de converter:\n"))
    seg = min * 60
    print(f"Seu valor em segundos é de {seg}")

else: 
    print("A opção escolhida inválida")
