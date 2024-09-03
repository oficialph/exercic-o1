preco_fabrica = float(input("Digite o preço de fábrica da peça (em R$): "))

percentual_acrescimo = 30

acrescimo = preco_fabrica * (percentual_acrescimo / 100)

preco_final = preco_fabrica + acrescimo

print(f"O valor final da peça é: R${preco_final:.2f}")