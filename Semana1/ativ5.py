import random

def determinarSigno(ano_de_nascimento):
    signos = {
        "Capricórnio": (1, 20, 12, 31),  # (mês_inicial, dia_inicial, mês_final, dia_final)
        "Aquário": (1, 21, 2, 18),
        "Peixes": (2, 19, 3, 20),
        "Áries": (3, 21, 4, 19),
        "Touro": (4, 20, 5, 20),
        "Gêmeos": (5, 21, 6, 20),
        "Câncer": (6, 21, 7, 22),
        "Leão": (7, 23, 8, 22),
        "Virgem": (8, 23, 9, 22),
        "Libra": (9, 23, 10, 22),
        "Escorpião": (10, 23, 11, 21),
        "Sagitário": (11, 22, 12, 21),
        "Capricórnio": (12, 22, 12, 31)  #últimos dias do ano
    }

    for signo, (mes_ini, dia_ini, mes_fim, dia_fim) in signos.items():
        if (ano_de_nascimento.month == mes_ini and ano_de_nascimento.day >= dia_ini) or \
           (ano_de_nascimento.month > mes_ini and ano_de_nascimento.month < mes_fim) or \
           (ano_de_nascimento.month == mes_fim and ano_de_nascimento.day <= dia_fim):
            return signo

#buscando o signo
from datetime import datetime

ano_nascimento = datetime(1994, 8, 11)
signo = determinarSigno(ano_nascimento)
print(f"O signo da pessoa nascida em {ano_nascimento.year} é {signo}.")

