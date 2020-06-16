#coding: utf-8

#Entrada de dados
n1 = int(input('Digite o numerador: '))
n2 = int(input('Digite o denominador: '))

#Processamento
if n2 == 0:
    print('Essa divisão é impossível')
else:
    divisao = n1 / n2

    #Saída de dados
    print('Os números foram divididos e o resultado foi', divisao)
