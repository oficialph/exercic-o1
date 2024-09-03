preco_pneu = 395.40

total_carros = int(input("Digite o total de carros da frota: "))

total_pneus = total_carros * 4

valor_final = total_pneus * preco_pneu

print(f"O valor total para trocar todos os pneus da frota é: R${valor_final:.2f}")