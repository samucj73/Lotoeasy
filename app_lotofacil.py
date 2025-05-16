import streamlit as st
from estatisticas_lotofacil import (
    dezenas_mais_sorteadas,
    dezenas_menos_sorteadas,
    trincas_mais_sorteadas,
    faixas_mais_sorteadas,
    linhas_mais_sorteadas,
    colunas_mais_sorteadas,
)
from gerador_lotofacil import gerar_cartoes
from util import exportar_pdf, exportar_txt
import matplotlib.pyplot as plt
from collections import Counter

st.set_page_config(page_title="Lotofácil Inteligente", layout="centered")
st.title("🍀 Lotofácil Inteligente")
st.markdown("Gere cartões e visualize estatísticas com base nos concursos reais.")

quantidade = st.slider("🎫 Quantos cartões deseja gerar?", 1, 10, 1)
cartoes = gerar_cartoes(quantidade)

st.subheader("🧾 Cartões Gerados")
for i, c in enumerate(cartoes, 1):
    st.success(f"Cartão {i}: {' - '.join(f'{d:02}' for d in c)}")

st.markdown("---")
st.subheader("📊 Estatísticas da Lotofácil (Últimos 10 Concursos)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🔝 Dezenas Mais Sorteadas")
    for dez, freq in dezenas_mais_sorteadas():
        st.write(f"Dezena **{dez:02}** → {freq}x")
with col2:
    st.markdown("### 🔻 Dezenas Menos Sorteadas")
    for dez, freq in dezenas_menos_sorteadas():
        st.write(f"Dezena **{dez:02}** → {freq}x")

st.markdown("---")
st.subheader("🔢 Faixas, Linhas e Colunas")

st.write("➡️ **Faixas mais sorteadas:**")
for faixa, freq in faixas_mais_sorteadas():
    st.write(f"Faixa {faixa} → {freq}x")

col3, col4 = st.columns(2)
with col3:
    st.write("📐 **Linhas mais sorteadas:**")
    for linha, freq in linhas_mais_sorteadas():
        st.write(f"Linha {linha} → {freq}x")
with col4:
    st.write("📏 **Colunas mais sorteadas:**")
    for coluna, freq in colunas_mais_sorteadas():
        st.write(f"Coluna {coluna} → {freq}x")

st.markdown("---")
st.subheader("🔺 Trincas Mais Sorteadas")
for trinca, freq in trincas_mais_sorteadas():
    st.write(f"Trinca {trinca} → {freq}x")

st.markdown("---")
st.subheader("📤 Exportar Jogos")

if cartoes:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬇️ Exportar .TXT"):
            caminho = exportar_txt(cartoes)
            st.success(f"Arquivo salvo como: {caminho}")
    with col2:
        if st.button("⬇️ Exportar .PDF"):
            caminho = exportar_pdf(cartoes)
            st.success(f"Arquivo salvo como: {caminho}")