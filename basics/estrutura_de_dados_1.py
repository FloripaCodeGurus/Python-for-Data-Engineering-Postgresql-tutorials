
## Estruturas de Dados
# Listas
# Listas sao estruturas de dados que armazenam uma colecao de dados
dados_pessoais = [      # lista
    1, # integers(inteiros)
    "Erick", # strigs(textos)
    "Classo",
    "Florianopolis",
    "Santa Catarina",
    "Brasil",
    "Ensino Medio incompleto",
    65.6,  # float # numeros decimais
]
# print(f"Dados pessoais: {dados_pessoais}")

nome = dados_pessoais[1]
sobrenome = dados_pessoais[2]
# print(f"Nome:{nome}")
# print(f"Sobrenome:{sobrenome}")

# LISTAS ACEITAM RECEBER NOVOS DADOS
# PARA  ADICIONAR NOVOS DADOS USAMOS O append()
telefone = "48 99999-9999"
dados_pessoais.append(telefone)
# print(f"Dados pessoais: {dados_pessoais}")
telefone_do_erick = dados_pessoais[8]
# print(f"Telefone do Erick: {telefone_do_erick}")

# PARA REMOVER DADOS USAMOS O pop()
dados_pessoais.pop(7) # indice na posicao 7 era o valor 65.6
# print("ESTRUTURA DE DADOS - LISTAS")
# print(f"Dados pessoais: {dados_pessoais}")

# ======================================
# TUPLAS () parenteses - immutaveis
# print("ESTRUTURA DE DADOS - TUPLAS")
# dados_pessoais_tuplas = (1, "Erick", "Classo", "Florianopolis", "Santa Catarina", "Brasil", "Ensino Medio incompleto")
# print(f"Dados pessoais: {dados_pessoais_tuplas}")
# telefone = "48 99999-9999"
# telefone_2 = "48 99888-9999"

# dados_pessoais_tuplas.append(telefone) # erro

# FORÇAR A TUPLA A SER IMUTAVEL
# print("ESTRUTURA DE DADOS - TUPLAS COPIA")
# dados_pessoais_tuplas_2 = dados_pessoais_tuplas + (telefone, telefone_2)
# print(type(dados_pessoais_tuplas_2))
# print(dados_pessoais_tuplas_2)

## DICIONARIOS {} - chave e valor
# print("ESTRUTURA DE DADOS - DICIONARIOS")

dados_pessoais_dict = {
    "id": 1,
    "nome": "Erick",
    "sobrenome": "Classo",
    "cidade": "Florianopolis",
    "estado": "Santa Catarina",
    "pais": "Brasil",
    "grau de ensino": "Ensino Medio incompleto",
    "telefone": "48 99999-9999",
    "telefone_2": "48 99888-9999",
}
nome = dados_pessoais_dict["nome"]
sobrenome = dados_pessoais_dict["sobrenome"]
estado = dados_pessoais_dict["estado"]

# print(f"Nome:{nome}")
# print(f"Sobrenome:{sobrenome}")
# print(f"Estado:{estado}")
# =======================================================================================================
# LISTAS
print("ESTRUTURA DE DADOS - LISTAS")

times_de_futebol = ['Flumnense'] # Um conjuntos de dades entre colchetes [], separados por virgulas
# adiçao, append()
times_de_futebol.append("Flamengo")
times_de_futebol.append("Palmeiras")
times_de_futebol.append("Vasco")
print(f"Times de futebol: {times_de_futebol}")

# insert
times_de_futebol.insert(0, "Santos") # Adiciona na posicao 0
print(f"Times de futebol: {times_de_futebol}")

# remoçao pop()
times_de_futebol.pop(0) # Remove o primeiro elemento
print(f"Times de futebol: {times_de_futebol}")

# delete del lista[]
del times_de_futebol[0] # Remove o primeiro elemento
print(f"Times de futebol: {times_de_futebol}")
times = len(times_de_futebol)
# =======================================================================================================
# TUPLAS 
print("ESTRUTURA DE DADOS - TUPLAS")
times_de_volei = () # Um conjuntos de dades entre parenteses (), separados por virgulas
# times_de_volei.__add__("Brasil") # Tuplas sao imutaveis, nao podemos adicionar novos dados ERRO
times_de_volei = times_de_volei + ("Brasil",) # Adiciona Brasil a tupla, time_de_volei vazio + ("Brasil",)
print(type(times_de_volei))
print(f"Times de volei: {times_de_volei}")
espanha = ("Espanha",) 

times_de_volei = times_de_volei + espanha # Adiciona Espanha a tupla
print(f"Times de volei: {times_de_volei}")
# checar a quantidade, len()
quantidade_de_time = len(times_de_volei) # Retorna a quantidade de elementos na tupla
print(f"Quantidade de times de volei: {quantidade_de_time}")

# remoçao
print(times_de_volei[:1])
times_de_volei = times_de_volei[:1] # Remove todos os elementos a partir do indice 1

# =======================================================================================================
# DICIONARIOS
times_de_basquete = {} # Um conjuntos de dados entre chaves {}, separados por virgulas , d = {key:value}
times_de_basquete = {
                        "Nome": "Chicago Bulls",
                        "Cidade": "Chicago",
                        "Estado": "Illinois",
                        "Pais": "Estados Unidos",
                        "Titulos": 6,
                        "Jogadores": ["Michael Jordan", "Scottie Pippen", "Dennis Rodman"] # lista
                    }
print()
print("ESTRUTURA DE DADOS - DICIONARIOS")
print(f"Times de basquete: {times_de_basquete}")
print()

print(f"Nome do time: {times_de_basquete['Nome']}")
print(f"Cidade do time: {times_de_basquete['Cidade']}")

# Adicionar novos dados, nome_do_dicionarios["chave"] = valor
times_de_basquete["Ano de fundacao"] = 1966
print(f"Times de basquete: {times_de_basquete}")
print()
#Remoção de dados
del times_de_basquete["Titulos"] # Remove a chave Titulos
print(f"Times de basquete: {times_de_basquete}")
print()

# Chaves keys()
print(f"Chaves do dicionario: {times_de_basquete.keys()}")

# Valores values()
print(f"Valores do dicionario: {times_de_basquete.values()}")
# =======================================================================================================
# SETS
print()
print("ESTRUTURA DE DADOS - SETS")