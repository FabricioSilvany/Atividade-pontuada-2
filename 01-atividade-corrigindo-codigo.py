import os
os.system("cls || clear")

# Variáveis para armazenar as estatísticas
QUANTIDADE_NUMEROS = 5
numeros_gerais = []
pares = []
impares = []
positivos = []
negativos = []

# Variáveis para armazenar os números
for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input(f"Digite o {i+1}º número: "))
    numeros_gerais.append(numeros)
    os.system("cls || clear")


# Processando os números
if numeros % 2 == 0:
    pares.append(numeros)
else:
    impares.append(numeros)

if numeros < 0:
    negativos.append(numeros)
else:
    positivos.append(numeros)

soma_geral = sum(numeros_gerais)


# Calculando as médias e armazenando as quantidades
quantidade_pares = len(pares)
quantidade_impares = len(impares)

if quantidade_pares == 0:
    media_pares = "Nada"
else:
    media_pares = sum(pares) / quantidade_pares

if quantidade_impares == 0:
    media_impares = "Nada"
else:
    media_impares = sum(impares) / quantidade_impares

# Exibindo dados
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {len(positivos)}")
print(f"Quantidade de negativos: {len(negativos)}")
print(f"Maior número: {max(numeros_gerais)}")
print(f"Menor número: {min(numeros_gerais)}")
print(f"Média dos números pares: {media_pares}")
print(f"Média dos números ímpares: {media_impares}")
print(f"Média de todos os números: {sum(numeros_gerais) / len(numeros_gerais)}")
numeros_gerais.reverse()
print(f"Números na ordem inversa: {numeros_gerais}")