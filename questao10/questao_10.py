import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

def grafico_atendimentos_por_dia(datas):
    
    datas_convertidas = []
    for data in datas:
        data_atual = datetime.strptime(data, "%Y-%m-%d").date()
        datas_convertidas.append(data_atual)
    
    contagem = Counter(datas_convertidas)
    
    dias = list(contagem.keys())
    quantidades = list(contagem.values())
    
    plt.bar(dias, quantidades, color='skyblue')
    plt.xlabel('Data')
    plt.ylabel('Quantidade de Atendimentos')
    plt.title('Quantidade de Atendimentos Médicos por Dia')
    plt.show()
    print(contagem)

entrada = [
    "2024-08-21",
    "2024-08-21",
    "2024-08-22",
    "2024-08-22",
    "2024-08-22",
    "2024-08-23"
]

grafico_atendimentos_por_dia(entrada)
