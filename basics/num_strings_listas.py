"""
Números
Strings
Listas
"""
#Numeros
inteiros = 10
decimais = 10.5

soma = inteiros + decimais
print(soma)

divisoes = 30 / 7
print(round(divisoes, 2))


# STRINGS /VARCHAR (texto)
nome = "Fabio"
print(type(nome)) # type é uma função que retorna o tipo de dado, <class 'str'>

idade = 30
print(type(idade)) # <class 'int'> inteiro, integer

peso = 80.5
print(type(peso)) # <class 'float'> ponto flutuante, decimal

cpf = "04747053856"
print(type(cpf)) # <class 'str'>, mesmo sendo um número, é tratado como string


# calculo
num_1 = "100"
num_2 = "200"

soma = num_1 + num_2
print(soma) 

num_1 = 100
num_2 = 200

soma = num_1 + num_2
print(soma) 


# LISTAS
lista = [1, 3,2,  4, 5] # UM CONJUNTO DE VALORES DENTRO DE [] COLCHETES, SEPARADOS POR VÍRGULAS
print(lista)  # imprime a lista completa
# Indice em Python sempre começa com 0
print(lista[0]) # imprime o primeiro elemento da lista

clubes = ["Flamengo", "Vasco", "Botafogo", "Fluminense"]
print(clubes[2])
print(f"time de perdedores: {clubes[2]}")  
print(f"time de derrotados: {clubes[1]}")  
# imprime o terceiro elemento da lista