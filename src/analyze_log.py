import csv
from collections import Counter
import os


def pratos_maria(client, content):
    lista_ped = []

    for item in content:
        if item[0] == client:
            lista_ped.append(item[1])

    return Counter(lista_ped).most_common(1)[0][0]


def count_arnaldo(content):
    total_prato = []

    for item in content:
        if item.split(",")[0] == "arnaldo" and item.split(",")[1] == "hamburguer":
            total_prato.append(item)

    return len(total_prato)


def uneaten_dishes_joao(content):
    list_pratos = set()
    lista_pratos_joao = set()

    for item in content:
        list_pratos.add(item.split(",")[1])

        if item.startswith("joao"):
            lista_pratos_joao.add(item.split(",")[1])

    new_value = list_pratos.difference(lista_pratos_joao)
    return new_value


def not_week_days(content):
    open_days = set()
    days_joao = set()

    for item in content:
        open_days.add(item.split(",")[2].replace("\n", ""))

        if item.startswith("joao"):
            days_joao.add(item.split(",")[2].replace("\n", ""))

    return open_days.difference(days_joao)


def analyze_log(path_to_file):
    extension = os.path.splitext(path_to_file)[1]

    if extension == '.csv':
        try:

            with open(path_to_file, "r") as file:
                file_content = file.readlines()

            not_days_joao = not_week_days(file_content)
            max_pedido_maria = pratos_maria(file_content)
            toral_pratos_arnaldo = count_arnaldo(file_content)
            dishes_joao = uneaten_dishes_joao(file_content)

            with open('data/mkt_campaign.txt', 'w', encoding="utf-8") as file:
                file.write(
                    f"{max_pedido_maria}\n{toral_pratos_arnaldo}\n{dishes_joao}\n{not_days_joao}")

        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
