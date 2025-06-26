# Idetificadores em Python

#1nome ="Erick"  # ERRADO
#1_nome = "Erick"  # ERRADO

nome1 = "Erick" # CORRETO
nome_1 = "Erick" # CORRETO

# print(nome1)

#camelCase
nomeDoUsuario = "Erick"  # CORRETO

#snake_case
nome_do_usuario = "Erick"  # CORRETO, nesse caso o nome_do_usuario  recebe o valor "Fabio" (= atribuição)

# palavras reservadas
# lambda = 10 # ERRADO
_lambda = 10 # CORRETO

# Identacao
if nome_do_usuario == 'Erick':  # == comparação
    print("Erick")
else:
    print("USUARIO DESCONHECIDO")

# comentatio de multiplas linas
'''
    Esse é um comentário de múltiplas linhas
    que pode ser usado para descrever
'''

"""
    Esse é um comentário de múltiplas linhas
    que pode ser usado para descrever
"""

a = 10
b = 10
c = 10

d = e = f = 20
print(a, b, c)
print(d, e, f)

print()
nome, sobrenome, idade, peso = "Fabio", "Classo", 30, 80.5
print(f"Nome: {nome} Sobrenome: {sobrenome} Idade: {idade} anos Peso: {peso} kg")