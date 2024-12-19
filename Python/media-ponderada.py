
nome = input("Insira o nome completo do aluno que irá receber as notas:\n")

n1 = int(input("Agora insira as 3 notas do aluno abaixo:\n"))
n2 = int(input(''))
n3 = int(input(''))

mediaPonderada = (n1 + n2 + n3 / 11)

print("O aluno", nome," tem média ponderada de", int(mediaPonderada))