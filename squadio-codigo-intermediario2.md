## Bootcamp Python Data Analytics<br>Desafios de Código SQUADIO - Intermediário II

### 1 / 3 - O Robô inteligente

* Básico
*Princípios Básicos

#### Desafio
Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

#### Entrada:
A entrada deve receber valores inteiros.

* **numero:** valor inteiro que pode ser positivo, negativo ou zero. Lembrando que a entrada zero deve encerrar o programa.

#### Saída:
O código deverá retornar uma mensagem (string) informando se o número é positivo ou não. Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos e negativos.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada | Saída
--- | ---
1<br>-1<br>2<br>0 | positivo!<br>negativo!<br>positivo!<br>2 números positivos, 1 números negativos
1<br>-1<br>0 | positivo!<br>negativo!<br>1 números positivos, 1 números negativos
1<br>1<br>-1<br>-1<br>0 | positivo!<br>positivo!<br>negativo!<br>negativo!<br>2 números positivos, 2 números negativos

```py
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
```

---

### 2 / 3 - A Jornada da Classificação Frutífera

* Básico
* Princípios Básicos

#### Descrição
Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

* Maçã:
  * Peso mínimo: 130 gramas
  * Textura: Ápera (rough)
  * Cor: Vermelha (red)

* Laranja:
  * Peso mínimo: 120 gramas
  * Textura: Suave (smooth)
  * Cor: Laranja (orange)

* Morango:
  * Peso mínimo: 150 gramas
  * Textura: Suave (smooth)
  * Cor: Vermelha (red)

* Banana:
  * Peso mínimo: 150 gramas
  * Textura: Áspera (rough)
  * Cor: Amarela (yellow)

#### Entrada
Seu código deve receber as seguintes entradas do usuário:

* Peso da fruta (em gramas): um número real que representa o peso da fruta.
* Textura da fruta (suave ou áspera): uma string indicando se a fruta é suave ("smooth") ou áspera ("rough").
* Cor da fruta (vermelha, laranja ou amarela): uma string indicando a cor da fruta.

#### Saída
O código deve produzir uma saída indicando a classificação da fruta com base nas características fornecidas.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada | Saída
--- | ---
150<br>smooth<br>red | A fruta é um morango!
140<br>rough<br>yellow | Não foi possível classificar a fruta.
150<br>smooth<br>orange | A fruta é uma laranja!

```py
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
```

---

### 3 / 3 - A Questão Intrincada da Magia Preditiva
* Intermediário
* Princípios Básicos

#### Descrição
No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos.

Aqui estão os critérios mágicos para cada elemento:

* Elemento Fogo:
  * Intensidade do feitiço maior ou igual a 5.
  * Fase lunar durante o feitiço é crescente.
  * Idade do feiticeiro é superior a 100 anos.

* Elemento Água:
  * Intensidade do feitiço maior ou igual a 7.
  * Presença de componente raro.
  * Fase lunar durante o feitiço é cheia.
  * Idade do feiticeiro é igual ou inferior a 100 anos.
  * Afinidade com animais mágicos.

* Elemento Terra:
  * Intensidade do feitiço maior ou igual a 7.
  * Presença de componente raro.
  * Fase lunar durante o feitiço é cheia.
  * Idade do feiticeiro é igual ou inferior a 100 anos.
  * Afinidade com animais mágicos.

* Elemento Ar:
  * Caso não se encaixe nos critérios anteriores.

#### Entrada
Seu código deve receber as seguintes entradas do usuário:
* Intensidade do feitiço (de 1 a 10): um número inteiro representando a força do feitiço.
* Componente raro (sim ou não): uma string indicando se o feitiço contém um componente raro.
* Fase lunar (cheia, crescente ou minguante): uma string indicando a fase lunar durante o lançamento do feitiço.
* Idade do feiticeiro (em anos): um número inteiro representando a idade do feiticeiro.
* Afinidade com animais mágicos (sim ou não): uma string indicando se o feiticeiro tem afinidade com animais mágicos.

#### Saída
O código deve produzir uma saída indicando a afinidade elemental prevista do feiticeiro com base nos atributos fornecidos.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada | Saída
--- | ---
6<br>sim<br>crescente<br>110<br>sim | A afinidade elemental do feiticeiro é com o elemento Fogo!
8<br>sim<br>cheia<br>80<br>não | A afinidade elemental do feiticeiro é com o elemento Água!
9<br>sim<br>cheia<br>80<br>sim | A afinidade elemental do feiticeiro é com o elemento Terra!

```py
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
```