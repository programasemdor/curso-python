#coding: utf-8

# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

#Entrada de dados
num_semana = int(input('Digite um número da semana: '))

#Processamento e Saída de Dados
if num_semana == 1:
    print('Domingo')
elif num_semana == 2:
    print('Segunda-feira')
elif num_semana == 3:
    print('Terça-feira')
elif num_semana == 4:
    print('Quarta-feira')
elif num_semana == 5:
    print('Quinta-feira')
elif num_semana == 6:
    print('Sexta-feira')
elif num_semana == 7:
    print('Sábado')
else:
    print('Valor Inválido')
