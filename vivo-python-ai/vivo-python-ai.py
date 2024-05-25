# ----------------------------------------
# Bootcamp Python AI Backend Developer<

# ----------------------------------------
# Dominando os Fundamentos Básicos do Python - Básico

# 1 / 3 - Verificador de Planos de Internet

def recomendar_plano(consumo):
    if consumo <= 10:
        return 'Plano Essencial Fibra - 50Mbps'
    elif consumo <= 20:
        return 'Plano Prata Fibra - 100Mbps'
    else:
        return 'Plano Premium Fibra - 300Mbps'

# Crie uma Estrutura Condicional para verifica o consumo médio mensal
# Retorne o plano de internet adequado:

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))


# 2 / 3 - Criando uma Lista de Equipamentos

# Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# Crie um loop para solicita os itens ao usuário:
for i in range(3):

    # Solicite o item e armazena na variável "item":
    item = input()

    # Adicione o item à lista "itens":
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for equipamento in itens:

    # Loop que percorre cada item na lista "itens"
    print(f"- {equipamento}")



# 3 / 3 - Validando Número de Telefone

# Módulo 're' que fornece operações com expressões regulares.
import re

# Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':

def validate_numero_telefone(phone_number):

    # Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    pattern = '\(\d{2}\) 9\d{4}-\d{4}'

    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):

        # Agora crie um return, para retornar que o número de telefone é válido:
        return 'Número de telefone válido.'

    else:
        # Crie um else e return, caso não o número de telefone seja inválido:
        return 'Número de telefone inválido.'


# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()

# Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)

# ----------------------------------------
