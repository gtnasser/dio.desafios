# Bootcamp Potência Tech powered by iFood | Ciência de Dados
# Exercite sua Lógica com Desafios de Código em Python

# ----------------------------------------
# Tempo Estimado de Entrega

nomeRestaurante = input()
tempoEstimadoEntrega = int(input())

saida = f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos."
print(saida)


# ----------------------------------------
# Calcular o Preço Final de um Pedido

valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

precoFinal = valorHamburguer * quantidadeHamburguer + valorBebida * quantidadeBebida
troco = valorPago - precoFinal
saida = f"O preço final do pedido é R$ {precoFinal:.2f}. Seu troco é R$ {troco:.2f}."

print(saida)

# ----------------------------------------
# Ganhe uma Sobremesa Especial!

valorPedido = float(input())

if valorPedido >= 50:
    mensagem = "Parabens, você ganhou uma sobremesa gratis!"
else :
    mensagem = "Que pena, você nao ganhou nenhum brinde especial."

# usando a interpolacao de strings
print(f"{mensagem}")

# ----------------------------------------
# Gerenciamento de Pedidos de Comida Online

def main():
    n = int(input())

    total = 0
    valor = 0

    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    cupom = input()
    desconto = 0
    if cupom == "10%":
        desconto = total * 0.9
    if desconto == "20%":
        desconto = total * 0.8
    total = total - desconto

    print(f"Valor total: {total:.2f}")

if __name__ == "__main__":
    main()

# ----------------------------------------
# Identificando Pedidos Veganos

numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()

    if ehVegano == "s":
        ehVeganoTexto = "Vegano"
    else:
        ehVeganoTexto = "Nao-vegano"

    print(f"Pedido {i}: {prato} ({ehVeganoTexto}) - {calorias} calorias")
