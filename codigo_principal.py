def processar_financas(valor_dividas, valor_ganho):
    valor_dividas_num = valor_dividas.lower().replace('+', ' ').replace(',', '.').split()
    valor_dividas_num = [float(item)for item in valor_dividas_num]
    valor_dividas_soma = sum(valor_dividas_num)

    valor_ganho_num = valor_ganho.lower().replace('+', ' ').replace(',', '.').split()
    valor_ganho_num = [float(item)for item in valor_ganho_num]
    valor_ganho_soma = sum(valor_ganho_num)

    valor_mensal = valor_ganho_soma - valor_dividas_soma
    return valor_dividas_soma, valor_ganho_soma, valor_mensal