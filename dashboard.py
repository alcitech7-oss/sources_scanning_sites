# dashboard.py
import streamlit as st
import pandas as pd
from datetime import datetime
from processador.consolidador import consolidar_dados
from utils.horario import status_pregao
from utils.formatador import formatar_moeda, formatar_ibovespa

st.set_page_config(page_title="Robô Financeiro", page_icon="📊", layout="wide")

st.title("📊 Robô Financeiro — Monitor de Cotações")
st.caption(f"Atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

st.info(status_pregao())

if st.button("🔄 Atualizar dados agora"):
    with st.spinner("Coletando cotações..."):
        dados = consolidar_dados()
        st.success("Dados atualizados!")

dados = consolidar_dados()

tabela = []
for moeda, fontes in dados.items():
    for fonte, valor in fontes.items():
        if moeda == "ibovespa":
            valor_formatado = formatar_ibovespa(valor)
            rotulo = "Valor (pontos)"
        else:
            valor_formatado = formatar_moeda(valor)
            rotulo = "Valor (R$)"
        tabela.append(
            {
                "Moeda": moeda.capitalize(),
                "Fonte": fonte,
                rotulo: valor_formatado,
                "Status": status_pregao(),
            }
        )

df = pd.DataFrame(tabela)

st.subheader("📋 Cotações atuais")
st.dataframe(df, use_container_width=True)

st.subheader("📈 Comparação entre fontes")
if not df.empty:
    for moeda in df["Moeda"].unique():
        if moeda != "Ibovespa":
            st.write(f"**{moeda}**")
            subset = df[df["Moeda"] == moeda]
            valores = []
            for _, row in subset.iterrows():
                v = row["Valor (R$)"].replace("R$ ", "").replace(",", ".")
                try:
                    valores.append(float(v))
                except:
                    valores.append(0)
            st.bar_chart(pd.Series(valores, index=subset["Fonte"]))

st.caption("Desenvolvido com ❤️ e Python")
