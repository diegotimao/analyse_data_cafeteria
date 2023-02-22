from collections import Counter
import os


def client_dishes(client, content):
    lista_ped = []

    for item in content:
        if item[0] == client:
            lista_ped.append(item[1])

    return Counter(lista_ped).most_common(1)[0][0]


def count_arnaldo(content):
    total_prato = []

    for item in content:
        if item.split(",")[0] == "arnaldo":
            if item.split(",")[1] == "hamburguer":
                total_prato.append(item)

    return len(total_prato)


def uneaten_client_dishes(client, content):
    list_dishes = set()
    lista_dishes_client = set()

    for item in content:
        list_dishes.add(item[1])

        if item[0] == client:
            lista_dishes_client.add(item[1])

    return list_dishes.difference(lista_dishes_client)


def not_week_days(client, content):
    open_days = set()
    days_joao = set()

    for item in content:
        open_days.add(item[2])

        if item[0] == client:
            days_joao.add(item[2])

    return open_days.difference(days_joao)


def analyze_log(path_to_file):
    extension = os.path.splitext(path_to_file)[1]

    if extension == '.csv':
        try:

            with open(path_to_file, "r") as file:
                file_content = file.readlines()

            not_days_joao = not_week_days("arnaldo", file_content)
            max_pedido_maria = client_dishes("maria", file_content)
            toral_pratos_arnaldo = count_arnaldo(file_content)
            dishes_joao = uneaten_client_dishes("joao", file_content)

            with open('data/mkt_campaign.txt', 'w', encoding="utf-8") as file:
                file.writelines(
                    f"{max_pedido_maria}\n",
                    f"{toral_pratos_arnaldo}\n",
                    f"{dishes_joao}\n",
                    f"{not_days_joao}")

        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
