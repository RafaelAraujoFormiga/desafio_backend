class CNAB:
    """Classe para criar um dict a partir de dados do arquivo CNAB.txt"""

    def __init__(
        self,
        type,
        date,
        value,
        cpf,
        card,
        hour,
        store_owner,
        store_name,
    ):
        self.type = int(type)
        self.date = f"{date[:4]}/{date[4:6]}/{date[6:8]}"
        self.value = int(value) / 100
        self.cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        self.card = card
        self.hour = f"{hour[:2]}:{hour[2:4]}:{hour[4:6]}"
        self.store_owner = store_owner
        self.store_name = store_name
