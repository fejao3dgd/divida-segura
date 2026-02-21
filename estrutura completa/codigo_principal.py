valor_dividas = input('coloque todos os valores de dividas (coloque todos os valores, e se for preciso somar use +)')
valor_ganho= input('coloque todos os valores de ganhos (coloque todos os valores, e se for preciso somar use +)')
valor_mensal = 0

def processar_financas(texto_dividas, texto_ganhos):
    valor_dividas_num = valor_dividas.lower().replace('+', ' ').replace(',', '.').split()
    valor_dividas_num = [float(item)for item in valor_dividas_num]
    valor_dividas_soma = sum(valor_dividas_num)

    valor_ganho_num = valor_ganho.lower().replace('+', ' ').replace(',', '.').split()
    valor_ganho_num = [float(item)for item in valor_ganho_num]
    valor_ganho_soma = sum(valor_ganho_num)

    print(f'o valor total das dividas é de {valor_dividas_soma:.2f}')
    print(f'o valor total de ganho no mes é de {valor_ganho_soma:.2f}')

    valor_mensal = valor_ganho_soma - valor_dividas_soma
    return valor_dividas_soma, valor_ganho_soma, valor_mensal

resultado = processar_financas(valor_dividas, valor_ganho)