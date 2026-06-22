# main.py
from processador.consolidador import consolidar_dados
from exportador.planilha import gerar_planilha
from utils.horario import status_pregao


def main():
    print("🚀 Iniciando coleta de dados...\n")
    dados = consolidar_dados()
    gerar_planilha(dados)
    print(f"\n📊 Status do pregão: {status_pregao()}")


if __name__ == "__main__":
    main()
