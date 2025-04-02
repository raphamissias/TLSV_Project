import csv
import glob
import os

def read_csv_contracts():
    csv_archives = glob.glob('**/*.csv', recursive=True)

    if not csv_archives:
        print("Nenhum arquivo csv encontrado")
        return

    for archive in csv_archives:
        try:
            with open(archive, "r", encoding="ISO-8859-1") as f:
                reader = csv.DictReader(f, delimiter=";")
                # print("Cabeçalhos", reader.fieldnames)

                contracts_arr = []
                for line in reader:
                    contract_number = line['Contrato']
                    contracts_arr.append(contract_number)

                # for item in formated_array:
                #     print(item)
                
                # Retorna os números do contrato da planilha
                return contracts_arr

        except Exception as e:
            print(f"Erro ao abrir o arquivo {archive}: {e}")

def contract_numbers():
    csv_archives = glob.glob('**/*.csv', recursive=True)

    if not csv_archives:
        print("Nenhum arquivo csv encontrado")
        return

    for archive in csv_archives:
        try:
            with open(archive, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                # print("Cabeçalhos", reader.fieldnames)

                formated_array = []
                for line in reader:
                    number_dict = line['Contrato']
                    formated_array.append(number_dict)

                print(formated_array)

                # for item in formated_array:
                #     print(item)

        except Exception as e:
            print(f"Erro ao abrir o arquivo {archive}: {e}")

dados = []

def save_csv():
    csv_format = f'"Motivo de Não Realizado","Contrato","Telefone","Bairro","Período Agendado"\n'

    # Nome do arquivo
    archive_name = "backlog.csv"

    headers = ["Motivo de Não Realizado","Contrato","Telefone","Bairro","Período Agendado"]

    # Salvando os dados em um arquivo CSV
    with open(archive_name, mode="w", newline="", encoding="utf-8") as archive:
        
        writer = csv.DictWriter(archive, fieldnames=headers)
        writer.writeheader()  # Escreve o cabeçalho
        writer.writerows(dados)

    print(f"Arquivo '{archive_name}' salvo com sucesso!")

def update_csv(**kwargs):
    # Adicionando um novo dicionário com as informações no formato esperado
    current_contract_info = {
        "Motivo de Não Realizado": kwargs.get('XA_NOTDONE_REASON', ''),
        "Contrato": kwargs.get('customer_number', ''),
        "Telefone": kwargs.get('ccell', ''),
        "Bairro": kwargs.get('XA_NEIGHBORHOOD', ''),
        "Período Agendado": kwargs.get('a_tsid', '')
    }

    dados.append(current_contract_info)
    