import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# quantidade de registros
n = 300

# data inicial
inicio = datetime(2025, 1, 1, 6, 0)

# listas para armazenar os dados
timestamps = []
umidade = []
temperatura = []
ph = []
nitrogenio = []
fosforo = []
potassio = []
chuva = []
status_irrigacao = []
volume_irrigacao = []

# valores iniciais realistas
u = np.random.uniform(50, 70)
t = np.random.uniform(20, 28)
ph_val = np.random.uniform(5.5, 6.8)
N = np.random.uniform(40, 80)
P = np.random.uniform(20, 40)
K = np.random.uniform(30, 70)

for i in range(n):
    current_time = inicio + timedelta(minutes=15 * i)
    timestamps.append(current_time)

    # Variação suave de temperatura
    t += np.random.uniform(-0.7, 0.7)
    temperatura.append(round(t, 2))

    # Variação suave de pH
    ph_val += np.random.uniform(-0.05, 0.05)
    ph.append(round(ph_val, 2))

    # Variação suave NPK
    N += np.random.uniform(-1, 1)
    P += np.random.uniform(-0.5, 0.5)
    K += np.random.uniform(-1, 1)
    nitrogenio.append(round(N, 1))
    fosforo.append(round(P, 1))
    potassio.append(round(K, 1))

    # Chuva eventual
    c = np.random.choice([0, 0.5, 1, 1.5, 5], p=[0.9, 0.03, 0.03, 0.03, 0.01])
    chuva.append(c)

    # Umidade
    if c > 0:
        u += np.random.uniform(1, 4)  # chuva aumenta umidade
    else:
        u += np.random.uniform(-1.5, 1)  # variação natural

    # Forçar limites
    u = max(20, min(95, u))
    umidade.append(round(u, 1))

    # Lógica da irrigação
    if u < 40:
        irrig = np.random.choice(["LIGADA", "DESLIGADA"], p=[0.7, 0.3])
    else:
        irrig = np.random.choice(["LIGADA", "DESLIGADA"], p=[0.1, 0.9])

    status_irrigacao.append(irrig)

    # Volume irrigado
    if irrig == "LIGADA":
        volume_irrigacao.append(round(np.random.uniform(5, 25), 1))
        u += np.random.uniform(1, 3)
    else:
        volume_irrigacao.append(0)

# Montar dataframe
df = pd.DataFrame({
    "timestamp": timestamps,
    "umidade": umidade,
    "temperatura": temperatura,
    "ph": ph,
    "nitrogenio": nitrogenio,
    "fosforo": fosforo,
    "potassio": potassio,
    "chuva": chuva,
    "status_irrigacao": status_irrigacao,
    "volume_irrigacao_L": volume_irrigacao
})

# Exportar
df.to_csv("sensores_fase2.csv", index=False)

print("Arquivo sensores_fase2.csv gerado com sucesso!")
