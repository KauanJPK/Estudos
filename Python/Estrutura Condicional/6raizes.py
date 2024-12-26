
coeficiente = []
for i in range (3):
    coe = float(input(f'nota {i + 1}:'))
    coeficiente.append(coe)
delta = float(coeficiente[1] * coeficiente[1] - 4 * coeficiente[0] * coeficiente[2])
if delta == 0:
    print('Raizes Unicas')
elif delta > 0:
    print("Raizes distintas")
else:
    print("Raizes imaginárias")