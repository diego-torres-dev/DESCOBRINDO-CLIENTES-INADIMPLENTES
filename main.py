from devedores import clientes_devedores


def descobrir_inadimplentes(clientes_devedores):
    """Retorna uma lista com os clientes inadimplentes

    Parâmetros:
    clientes_devedores (list): lista de clientes devedores

    Retorna:
    lista_inadimplentes (list): lista de clientes inadimplentes
    """

    # Lista de clientes inadimplentes
    lista_inadimplentes = []

    # Percorre a lista de clientes devedores
    for cpf, divida, dias_atraso in clientes_devedores:

        # Verifica se o cliente deve mais de R$ 1 mil há mais de 20 dias
        if divida > 1000 and dias_atraso > 20:
            lista_inadimplentes.append(cpf)
        else:
            pass

    return lista_inadimplentes


inadimplentes = descobrir_inadimplentes(clientes_devedores)
print(f"Há {len(inadimplentes)} clientes inadimplentes.")
print("São estes:")
print("\n".join(inadimplentes))
