# Bootcamp Python Data Analytics

# ----------------------------------------
# Desafios de Código SQUADIO - Iniciante
# 1 / 3 - A Aventura do Explorador

while True:

  quantidade_passos = int(input())

  if quantidade_passos>0:
    for passo in range(quantidade_passos):
      plural='s' if passo>0 else '' 
      print(f"Explorador: {passo+1} passo{plural}")
  else:
    print("Nenhum passo dado na floresta.")

# ----------------------------------------
# 2 / 3 - Lista de itens

# Lista para armazenar os itens
itens = []

# Solicite os itens ao usuário
for i in range(3):
  item = input()
  itens.append(item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")

# ----------------------------------------
# 3 / 3 - Armazenamento de Dados é Vida!

capacidade_atual, aumento_percentual = map(int, input().split())

# nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual * (1 + aumento_percentual/100)

# Imprima a nova capacidade
print(int(nova_capacidade))


# ----------------------------------------
# Desafios de Código SQUADIO - Intermediário
# 1 / 3 - O Grande Depósito - Solucionando Problemas Bancários

valor = float(input())
saldo = 0

if valor > 0:
  # Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
  saldo = saldo + valor
  print("Deposito realizado com sucesso!")
  print(f"Saldo atual: R$ {saldo:.2f}")

elif valor < 0:
  # Imprimir a mensagem de valor inválido.
  print("Valor invalido! Digite um valor maior que zero.")

else:
  # Imprimir a mensagem de encerrar o programa.
  print("Encerrando o programa...")


# ----------------------------------------
### 2 / 3 - Estrutura de Dados: Organizando Os Seus Ativos

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
ativos = []
for _ in range(quantidadeAtivos):
  codigoAtivo = input()
  ativos.append(codigoAtivo)

# Ordenar os ativos em ordem alfabética
ativos.sort()

# Imprimir a lista de ativos ordenada
for i in range(quantidadeAtivos):
    print(ativos[i])


# ----------------------------------------
###3 / 3 - Validando a Força de Senhas no IAM

import re

# Faz as validacoes das regras na senha
def verificar_forca_senha(senha):

  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  # 1. A senha deve ter no mínimo 8 caracteres.
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  # 2. A senha deve conter pelo menos uma letra maiúscula (A-Z) -> testando com o regex "(?=.*[A-Z])"
  # 3. A senha deve conter pelo menos uma letra minúscula (a-z) -> testando com o regex "(?=.*[a-z])" 
  # 4. A senha deve conter pelo menos um número (0-9) -> testando com o regex "(?=.*[0-9])"
  # 5. A senha deve conter pelo menos um caractere especial -> testando com o regex "(?=.*\W)"
  pattern = re.compile("(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\W)")
  if not pattern.match(senha):
     return 'Sua senha nao atende aos requisitos de seguranca.'

  return 'Sua senha atende aos requisitos de seguranca. Parabens!'

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)


# ----------------------------------------
# Desafios de Código SQUADIO - Intermediário II
# 1 / 3 - O Robô inteligente

# Função para classificar um número como positivo ou negativo
def classificar_numero(numero):
  return 'positivo!' if numero>0 else 'negativo!' 
    
def main():
  positivos = 0
  negativos = 0

  while True:
    numero = int(input())

    # Encerra o loop se o usuário digitar 0.
    if numero == 0:
      # Imprime a quantidade de números positivos e negativos inseridos
      print(f"{positivos} números positivos, {negativos} números negativos")
      break  

    # Chama a função classificar_numero para imprimir a classificação do número
    tipo = classificar_numero(numero)
    print(tipo)

    # registra quantos números positivos e negativos foram inseridos
    if tipo == 'positivo!': 
      positivos += 1
    else:
      negativos += 1


if __name__ == "__main__":
    main()

# ----------------------------------------
# 2 / 3 - A Jornada da Classificação Frutífera


# Função para prever a classe da fruta
def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 130 and textura == "rough" and cor == "red":
      return "A fruta é uma maçã!"
    if peso >= 120 and textura == "smooth" and cor == "orange":
      return "A fruta é uma laranja!"
    if peso >= 150 and textura == "smooth" and cor == "red":
      return "A fruta é um morango!"
    if peso >= 150 and textura == "rough" and cor == "yellow":
      return "A fruta é uma banana!"

    return "Não foi possível classificar a fruta."

# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)


# ----------------------------------------
# 3 / 3 - A Questão Intrincada da Magia Preditiva

# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):

    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro == "sim"
    afinidade_animais = afinidade_animais == "sim"

    # Desenvolva a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
      return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    if intensidade >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100 and componente_raro and not afinidade_animais:
      return "A afinidade elemental do feiticeiro é com o elemento Água!"
    if intensidade >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100 and componente_raro and afinidade_animais:
      return "A afinidade elemental do feiticeiro é com o elemento Terra!"
  
    return "A afinidade elemental do feiticeiro é com o elemento Ar!"

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input().lower()
fase_lunar_feitico = input().lower()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input().lower()

# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão
print(resultado)

