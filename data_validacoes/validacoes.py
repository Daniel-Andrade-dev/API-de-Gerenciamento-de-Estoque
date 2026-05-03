from datetime import datetime


def gerar_data_agora() -> str:
    return datetime.now().strftime("%d/%m/%Y")

def gerar_horario_agora() -> str:
    return datetime.now().strftime("%H:%M")

def validar_campos(produto, preco, quantidade) -> bool:
    return False if not produto or not preco or not quantidade else True

def validar_preco_quantidade(preco, quantidade) -> bool:
    if preco <= 0:
        return False
    if quantidade < 0:
        return False
    return True