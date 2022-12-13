# CÁLCULO DE MÉDIA GEOMÉTRICA

import os
os.system('cls||clear')

while True:  # loop caso a nota seja negativa
    print('CÁLCULO DE MÉDIA GEOMÉTRICA')
    nota1 = float(input('Digite a primeira nota: '))
    if nota1 < 0:
        os.system('cls||clear')
        print('Você digitou uma nota negativa!\n')
        print('Digite a nota novamente')
        continue
    else:
        break

while True:  # loop caso a nota seja negativa
    nota2 = float(input('Digite a segunda nota: '))
    if nota2 < 0:
        os.system('cls||clear')
        print('Você digitou uma nota negativa!\n')
        print('Digite a nota novamente')
        continue
    else:
        break

while True:  # loop caso a falta seja negativa
    faltas = int(input('Quantidade de faltas: '))
    if faltas < 0:
        os.system('cls||clear')
        print('Faltas não podem ser negativas, digite novamente:')
        continue
    else:
        break

media = (nota1*nota2)**(1/2)  # cálculo da média geométrica

if faltas >= 20:
    print('Aluno reprovado por faltas!')
elif media <= 3:
    print('Aluno reprovado por nota!')
elif media < 6:
    if media > 3:
        print('Aluno de exame!')
elif media > 6:
    print('Aluno aprovado')
