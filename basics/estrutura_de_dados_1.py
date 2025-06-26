
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
print(f"Nome:{nome}")
print(f"Sobrenome:{sobrenome}")

# LISTAS ACEITAM RECEBER NOVOS DADOS
# PARA  ADICIONAR NOVOS DADOS USAMOS O append()
telefone = "48 99999-9999"
dados_pessoais.append(telefone)
# print(f"Dados pessoais: {dados_pessoais}")
telefone_do_erick = dados_pessoais[8]
print(f"Telefone do Erick: {telefone_do_erick}")

# PARA REMOVER DADOS USAMOS O pop()
dados_pessoais.pop(7) # indice na posicao 7 era o valor 65.6
print("ESTRUTURA DE DADOS - LISTAS")
print(f"Dados pessoais: {dados_pessoais}")

# ======================================
# TUPLAS () parenteses - immutaveis
print("ESTRUTURA DE DADOS - TUPLAS")
dados_pessoais_tuplas = (1, "Erick", "Classo", "Florianopolis", "Santa Catarina", "Brasil", "Ensino Medio incompleto")
print(f"Dados pessoais: {dados_pessoais_tuplas}")
telefone = "48 99999-9999"
telefone_2 = "48 99888-9999"

# dados_pessoais_tuplas.append(telefone) # erro

# FORÇAR A TUPLA A SER IMUTAVEL
print("ESTRUTURA DE DADOS - TUPLAS COPIA")
dados_pessoais_tuplas_2 = dados_pessoais_tuplas + (telefone, telefone_2)
print(type(dados_pessoais_tuplas_2))
print(dados_pessoais_tuplas_2)

## DICIONARIOS {} - chave e valor
print("ESTRUTURA DE DADOS - DICIONARIOS")

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

print(f"Nome:{nome}")
print(f"Sobrenome:{sobrenome}")
print(f"Estado:{estado}")
