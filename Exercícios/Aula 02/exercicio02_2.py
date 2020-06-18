#coding: utf-8

# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
# triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#
#     Dicas:
#
#     * Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#     * Triângulo Equilátero: três lados iguais;
#     * Triângulo Isósceles: quaisquer dois lados iguais;
#     * Triângulo Escaleno: três lados diferentes;

#Entrada de dados
lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

#Processamento e Saída de dados
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 == lado2 and lado2 == lado3:
        print('Triângulo Equilátero')
    elif (lado1 == lado2 and lado1 != lado3) or (lado2 == lado1 and lado2 != lado3) or (lado3 == lado1 and lado3 != lado2):
        print('Triângulo Isóceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Triângulo impossível!')
