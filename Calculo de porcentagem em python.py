valor = float(input('Valor do item: '))
qtd = int(input('Quantidade: '))
total = valor * qtd
desconto = total * 0.1
total_final = total - desconto
print(f'total com desconto: R$ {total_final:.2f}')

