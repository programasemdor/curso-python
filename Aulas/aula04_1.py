#coding: utf-8

i = 2
primo = True

#Entrada de dados
numero = int(input('Digite um número: '))

#Processamento
while i < numero:
    if numero % i == 0:
        primo = False
    i += 1

#Saída de dados
if primo:
    print('É um número primo')
else:
    print('Não é um número primo')
