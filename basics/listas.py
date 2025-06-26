
dados_pessoais = [1, "Erick", "Classo", "Florianopolis", "Santa Catarina", "Brasil", "Ensino Medio incompleto"]
dados_pessoais_2 = [2, "Giovanna", "Classo", "Florianopolis", "Santa Catarina", "Brasil", "Ensino Medio incompleto"]

print(f"Dados pessoais: {dados_pessoais}")
print()

print(f"Nome:{dados_pessoais[1]}")
print(f"Sobrenome:{dados_pessoais[2]}")
print(f"Cidade:{dados_pessoais[3]}")
print(f"grau de ensino:{dados_pessoais[6]}")
print(f"grau de ensino:{dados_pessoais[-1]}")  # ultimo elemento

print()
# invertendo a lista
print(f"Dados pessoais invertidos: {dados_pessoais[::-1]}")

print(type(dados_pessoais))
 
l2 = list("Erick")
print(type(l2))

# For loop

print(list(range(10))) # 0,1,2,3,..9


for numero in range(10): # 0,1,2,3,..9
    print(numero)

print()
for dados in dados_pessoais:
    print(dados)

for dados in dados_pessoais_2:
    print(dados)
print()

for e,g in zip(dados_pessoais, dados_pessoais_2):
    print(f"Dados do Erick: {e},===  Dados da Gigi: {g}")