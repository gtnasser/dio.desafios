## Python AI Backend Developer<br>Dominando os Fundamentos Básicos do Python - Básico


### 1 / 3 - Verificador de Planos de Internet
* Básico
* Princípios Básicos

#### Desafio
Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

Planos Oferecidos:

- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

#### Entrada
Como entrada solicite o consumo médio mensal de dados em GB (float).

#### Saída
Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
10

Plano Essencial Fibra - 50Mbps

19

Plano Prata Fibra - 100Mbps
21

Plano Premium Fibra - 300Mbps


# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

def recomendar_plano(consumo):
  if consumo <= 10:
    return 'Plano Essencial Fibra - 50Mbps'
  elif consumo<=20:
    return 'Plano Prata Fibra - 100Mbps'
  else:
    return 'Plano Premium Fibra - 300Mbps'

# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
# TODO: Retorne o plano de internet adequado:

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))

-----

Dominando os Fundamentos Básicos do Python
2 / 3 - Criando uma Lista de Equipamentos
* Básico
* Princípios Básicos

#### Desafio
Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

#### Entrada
O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

#### Saída
Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Antena
Roteador
Switch

Lista de Equipamentos:
- Antena
- Roteador
- Switch


Servidor
Cabinet Rack
Access Point
 	Lista de Equipamentos:
- Servidor
- Cabinet Rack
- Access Point
Edge Routers
Patch Cord
UPS

Lista de Equipamentos:
- Edge Routers
- Patch Cord
- UPS


# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicita os itens ao usuário:
for i in range(3):

  # TODO: Solicite o item e armazena na variável "item":
  item = input()

  # TODO: Adicione o item à lista "itens":
  itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for equipamento in itens:

    # Loop que percorre cada item na lista "itens"
    print(f"- {equipamento}")



Dominando os Fundamentos Básicos do Python
3 / 3 - Validando Número de Telefone





 Básico
 Estrutura de Dados
Desafio
Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

Formato esperado:
O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.

Entrada
Uma string representando o número de telefone.

Saída
Uma mensagem indicando se o número de telefone é válido ou inválido.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
(88) 98888-8888

Número de telefone válido.


(11)91111-1111	Número de telefone inválido.
225555-555

Número de telefone inválido.


