nome = input("Insira o nome completo do aluno que irá receber as notas:\n")
notas = []
print('Insira 3 notas para esse aluno')
for i in range(3):
    nota = float(input(f'nota {i + 1}:'))
    notas.append(nota)
pesos= [4,3,3]
mediap = sum(nota*peso for nota, peso in zip(notas,pesos))/sum(pesos)
if mediap >= 5:
    print(f'O aluno(a) {nome} obteve media ponderada de: {mediap:.2f}, e está aprovado!')
else:
    print(f'O aluno(a) {nome} obteve media ponderada de: {mediap:.2f} e está reprovado!')