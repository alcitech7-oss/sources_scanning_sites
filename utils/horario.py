# utils/horario.py
from datetime import datetime


def status_pregao():
    agora = datetime.now()
    hora = agora.hour

    if 10 <= hora < 17:
        return "🟢 Pregão aberto"
    elif hora < 10:
        return "🟡 Aguardando abertura do pregão"
    else:
        return "🔴 Pregão fechado — cotação congelada"
