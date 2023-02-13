import csv
from collections import Counter
import os
# Qual o prato mais pedido por 'maria'?
# Quantas vezes 'arnaldo' pediu 'hamburguer'?

# Quais pratos 'joao' nunca pediu?
# Quais dias 'joao' nunca foi à lanchonete?

def pratos_maria(content):
    lista_ped = []

    for item in content:
        if item["cliente"] == 'maria':
            lista_ped.append(item["prato"])

    values = Counter(lista_ped).most_common(1)[0][0]

    return values


def analyze_log(path_to_file):
    extension = os.path.splitext(path_to_file)[1]
    
    if extension == '.csv':
        try:
            with open(path_to_file) as file:
                file_csv = csv.DictReader(file, fieldnames=["cliente", "prato", "dia"])
                max_pedido_maria = pratos_maria(file_csv)


            with open('data/mkt_campaign.txt', 'w') as file:
                file.write(max_pedido_maria)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    

    




    

