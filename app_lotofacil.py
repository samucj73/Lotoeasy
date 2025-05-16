import streamlit as st
from lotofacil_estatisticas import (
    dezenas_mais_sorteadas,
    dezenas_menos_sorteadas,
    trincas_mais_frequentes,
    linhas_mais_frequentes,
    colunas_mais_frequentes,
    faixas_mais_frequentes,
    ultimos_resultados
)
from estatisticas_adicionais import (
    pares_impares,
    soma_das_dezenas,
    quadrantes,
    sequencias_comuns,
    duplas_mais_comuns,
    repeticoes_com_concursos,
    dezenas_atrasadas
)
from util import exportar_txt, exportar_pdf
from gerador_lotofacil import gerar_cartoes_personalizados

st.set_page_config(page_title="LotoFácil Inteligente", layout="wide")

st.markdown("<h1 style='text-align: center;'>🍀 LotoFácil Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Gere cartões com base em estatísticas reais e personalização</p>", unsafe_allow_html=True)

# Geração
st.markdown("### 🎯 Geração de Cartões")
qtd_cartoes = st.slider("Quantos cartões deseja gerar?", 1, 100, 1)

fixas = st.multiselect("Escolha até 7 dezenas fixas:", list(range(1, 26)))
excluir = st.multiselect("Deseja excluir até 5 dezenas?", [i for i in range(1, 26) if i not in fixas])

if len(fixas) > 7:
    st.warning("Máximo de 7 dezenas fixas permitidas.")
elif len(excluir) > 5:
    st.warning("Máximo de 5 dezenas para excluir.")
elif st.button("🔁 Gerar Cartões"):
    cartoes = gerar_cartoes_personalizados(fixas, excluir, qtd_cartoes)
    cartoes_unicos = []
    vistos = set()
    for c in cartoes:
        chave = tuple(sorted(c))
        if chave not in vistos:
            cartoes_unicos.append(c)
            vistos.add(chave)
        if len(cartoes_unicos) >= qtd_cartoes:
            break
    for i, cartao in enumerate(cartoes_unicos, 1):
        st.success(f"Cartão {i}: {' - '.join(f'{n:02}' for n in sorted(cartao))}")
    st.session_state['cartoes'] = cartoes_unicos

# Estatísticas organizadas em abas
st.markdown("---")
st.subheader("📊 Análise Estatística")
abas = st.tabs([
    "Mais / Menos Sorteadas", "Trincas e Faixas", "Linhas / Colunas",
    "Pares e Ímpares", "Somas", "Quadrantes", "Sequências e Duplas",
    "Repetições", "Dezenas Atrasadas", "Últimos Resultados"
])

ultimos = [dezenas for _, dezenas in ultimos_resultados()]

with abas[0]:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Mais Sorteadas:**")
        for dez, freq in dezenas_mais_sorteadas():
            st.write(f"{dez:02}: {freq}x")
    with col2:
        st.markdown("**Menos Sorteadas:**")
        for dez, freq in dezenas_menos_sorteadas():
            st.write(f"{dez:02}: {freq}x")

with abas[1]:
    st.markdown("**Trincas Mais Frequentes:**")
    for trio, freq in trincas_mais_frequentes():
        st.write(f"{trio}: {freq}x")
    st.markdown("**Faixas Mais Frequentes:**")
    for faixa, freq in faixas_mais_frequentes():
        st.write(f"{faixa}: {freq}x")

with abas[2]:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Linhas Mais Frequentes:**")
        for linha, freq in linhas_mais_frequentes():
            st.write(f"{linha}: {freq}x")
    with col2:
        st.markdown("**Colunas Mais Frequentes:**")
        for col, freq in colunas_mais_frequentes():
            st.write(f"{col}: {freq}x")

with abas[3]:
    st.markdown("**Distribuição Pares e Ímpares:**")
    for (pares, impares), freq in pares_impares(ultimos):
        st.write(f"{pares} pares / {impares} ímpares: {freq}x")

with abas[4]:
    st.markdown("**Faixas de Soma das Dezenas:**")
    for faixa, freq in soma_das_dezenas(ultimos):
        st.write(f"Soma ~{faixa}-{faixa+9}: {freq}x")

with abas[5]:
    st.markdown("**Aparições por Quadrante:**")
    for q, freq in quadrantes(ultimos):
        st.write(f"Quadrante {q}: {freq}x")

with abas[6]:
    st.markdown("**Sequências Mais Comuns (3+ dezenas):**")
    for seq, freq in sequencias_comuns(ultimos):
        st.write(f"{seq}: {freq}x")
    st.markdown("**Duplas Mais Frequentes:**")
    for dupla, freq in duplas_mais_comuns(ultimos):
        st.write(f"{dupla}: {freq}x")

with abas[7]:
    st.markdown("**Repetição de Dezenas entre Concursos:**")
    for repetidas, freq in repeticoes_com_concursos(ultimos):
        st.write(f"{repetidas} repetidas: {freq}x")

with abas[8]:
    st.markdown("**Dezenas Ausentes nos Últimos 10 Concursos:**")
    atrasadas = dezenas_atrasadas(ultimos)
    st.write(", ".join(f"{d:02}" for d in atrasadas) if atrasadas else "Nenhuma dezena atrasada")

with abas[9]:
    st.markdown("**Últimos 10 Resultados da LotoFácil:**")
    for concurso, dezenas in ultimos_resultados():
        st.markdown(f"**Concurso {concurso}:** {' - '.join(f'{n:02}' for n in dezenas)}")

# Exportação
st.markdown("---")
st.subheader("📤 Exportar Cartões")
if st.session_state.get('cartoes'):
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬇️ Exportar .TXT"):
            caminho = exportar_txt(st.session_state['cartoes'])
            st.success(f"Salvo em {caminho}")
    with col2:
        if st.button("⬇️ Exportar .PDF"):
            caminho = exportar_pdf(st.session_state['cartoes'])
            st.success(f"Salvo em {caminho}")
else:
    st.info("Gere cartões antes de exportar.")

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Desenvolvido por <strong>SAMUCJ TECHNOLOGY</strong> 💡</p>", unsafe_allow_html=True)
