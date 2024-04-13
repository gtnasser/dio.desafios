## Bootcamp Python Data Analytics<br>Desafios de Código SQUADIO - Intermediário

### 1 / 3 - O Grande Depósito - Solucionando Problemas Bancários

* Básico
* Matemática

#### Desafio

Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro. O programa deve solicitar apenas uma vez o valor de depósito.

#### Entrada

O programa deve receber o valor de depósito digitado pelo cliente. Os valor pode ser decimal, representando valor em reais.

#### Saída

O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Se o valor for "0", deverá imprimir uma mensagem encerrando o programa. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro solicitando um novo valor.

#### Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada | Saída
--- | --- 
500.50 | Deposito realizado com sucesso!<br>Saldo atual: R$ 500.50
-100 | Valor invalido! Digite um valor maior que zero.
0 | Encerrando o programa...

```py

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


```

---

### 2 / 3 - Estrutura de Dados: Organizando Os Seus Ativos

* Básico
* Princípios Básicos

#### Descrição

Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancaria, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

#### Entrada

A primeira entrada consiste em um número inteiro que representa a  quantidade de ativos que o usuário possui. Em seguida, o usuário deverá  informar, em linhas separadas, os tipos (strings) dos respectivos ativos.

#### Saída
Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada | Saída
--- | ---
3<br>Financiamento de Imovel<br>Deposito<br>Reservas Bancarias | Deposito<br>Financiamento de Imovel<br>Reservas Bancarias
3<br>Carteiras de credito<br>Investimentos em titulos<br>Derivativos financeiros | Carteiras de credito<br>Derivativos financeiros<br>Investimentos em titulos
3<br>Reservas de liquidez<br>Ativos intangiveis<br>Fundos de investimento | Ativos intangiveis<br>Fundos de investimento<br>Reservas de liquidez

```py

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

```

---

###3 / 3 - Validando a Força de Senhas no IAM

* Intermediário
* Princípios Básicos

#### Desafio

Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa. Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

Requisitos de segurança para a senha:

1. A senha deve ter no mínimo 8 caracteres.
2. A senha deve conter pelo menos uma letra maiúscula (A-Z).
3. A senha deve conter pelo menos uma letra minúscula (a-z).
4. A senha deve conter pelo menos um número (0-9).
5. A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.

Saiba mais sobre o Regex em: [Java Regular Expressions](https://www.w3schools.com/java/java_regex.asp)

#### Entrada

A entrada será uma única string representando a senha que precisa ser validada.

#### Saída

Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.

Entrada | Saída
--- | ---
0101	Sua senha e muito curta. Recomenda-se no minimo 8 caracteres.
030609saturno*	Sua senha atende aos requisitos de seguranca. Parabens!
010203Jupiter	Sua senha nao atende aos requisitos de seguranca.

```py

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

```