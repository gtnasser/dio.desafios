## Bootcamp Python Data Analytics<br>Desafios de Código SQUADIO - Iniciante

### 1 / 3 - A Aventura do Explorador

* Básico
* Estrutura de Dados

#### Desafio
Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

#### Entrada
Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta. .

#### Saída
O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	| Saída
--- | ---
2 | Explorador: 1 passo<br>Explorador: 2 passos
3 | Explorador: 1 passo<br>Explorador: 2 passos<br>Explorador: 3 passos
0 | Nenhum passo dado na floresta.

```py
while True:

  quantidade_passos = int(input())

  if quantidade_passos>0:
    for passo in range(quantidade_passos):
      plural='s' if passo>0 else '' 
      print(f"Explorador: {passo+1} passo{plural}")
  else:
    print("Nenhum passo dado na floresta.")
```

---

### 2 / 3 - Lista de itens

* Básico
* Princípios Básicos

#### Desafio
Em um jogo de RPG, os personagens geralmente possuem uma lista de itens que podem ser utilizados durante o jogo. Esses itens podem ser armas, armaduras, poções de cura, entre outros. É importante que o jogador tenha um controle desses itens para poder utilizá-los no momento adequado.

Crie um programa que permita cadastrar uma lista de itens que o personagem possui. A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

#### Entrada
O programa deve solicitar ao usuário o nome dos 3 itens que o personagem possui. Cada item deve ser cadastrado separadamente.

#### Saída
Após receber os itens cadastrados pelo usuário, o programa deve exibir na tela a lista de itens que o personagem possui. A saída deve ter o seguinte formato:

```
Lista de itens:
- [item1]
- [item2]
- [item3]
```


#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	| Saída
--- | ---
Espada<br>EscudoPoção | Lista de itens:<br>- Espada<br>- Escudo<br>- Poção
Gema<br>Flecha<br>Capa | Lista de itens:<br>- Gema<br>- Flecha<br>- Capa
Masterball<br>Potion<br>Elixir | Lista de itens:<br>- Masterball<br>- Potion<br>- Elixir

``` py
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
```

---

### 3 / 3 - Armazenamento de Dados é Vida!
* Básico
* Matemática

#### Descrição
Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético, agora a mineração está muito mais eficiente! Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

#### Entrada
Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço.

#### Saída
A nova capacidade total em teraflops.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada | Saída
--- | ---
100 20 | 120
50 10 | 55
200 50 | 300

```py
capacidade_atual, aumento_percentual = map(int, input().split())

# nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual * (1 + aumento_percentual/100)

# Imprima a nova capacidade
print(int(nova_capacidade))
```
