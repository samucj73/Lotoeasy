
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
    dezenas_atrasadas,
    quantidade_primos
)
from util import exportar_txt, exportar_pdf
from gerador_lotofacil import gerar_cartoes_personalizados
from gerador_inteligente import gerar_cartoes_inteligentes

st.set_page_config(page_title="LotoFácil Inteligente", layout="wide")
st.markdown("<h1 style='text-align: center;'>🍀 LotoFácil Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Gere cartões com base em estatísticas reais e personalização</p>", unsafe_allow_html=True)

st.markdown("### 🎯 Geração de Cartões")
qtd_cartoes = st.slider("Quantos cartões deseja gerar?", 1, 100, 1)
fixas = st.multiselect("Escolha até 7 dezenas fixas:", list(range(1, 26)))
excluir = st.multiselect("Deseja excluir até 5 dezenas?", [i for i in range(1, 26) if i not in fixas])
modo_inteligente = st.checkbox("Usar geração inteligente com base nas estatísticas")

if len(fixas) > 7:
    st.warning("Máximo de 7 dezenas fixas permitidas.")
elif len(excluir) > 5:
    st.warning("Máximo de 5 dezenas para excluir.")
elif st.button("🔁 Gerar Cartões"):
    ultimos = list(ultimos_resultados())
    jogos = [(c, d, l) for c, d, l in ultimos]
    if modo_inteligente:
        mais_frequentes = [d[0] for d in dezenas_mais_sorteadas()]
        atrasadas = dezenas_atrasadas(jogos)
        cartoes = gerar_cartoes_inteligentes(qtd_cartoes, fixas, excluir, mais_frequentes, atrasadas)
    else:
        ult_dezenas = [l for _, _, l in ultimos]
        cartoes = gerar_cartoes_personalizados(fixas, excluir, qtd_cartoes, ult_dezenas)
    for i, cartao in enumerate(cartoes, 1):
        st.success(f"Cartão {i}: {' - '.join(f'{n:02}' for n in sorted(cartao))}")
    st.session_state['cartoes'] = cartoes

st.markdown("---")
st.subheader("📊 Estatísticas")

ultimos = list(ultimos_resultados())
jogos = [(c, d, l) for c, d, l in ultimos]

abas = st.tabs([
    "Mais / Menos Sorteadas", "Trincas e Faixas", "Linhas / Colunas",
    "Pares e Ímpares", "Somas", "Quadrantes", "Sequências e Duplas",
    "Repetições", "Dezenas Atrasadas", "Números Primos", "Últimos Resultados"
])

with abas[0]:
    st.markdown("**Mais Sorteadas:**")
    for dez, freq in dezenas_mais_sorteadas():
        st.write(f"{dez:02}: {freq}x")
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
    st.markdown("**Linhas Mais Frequentes:**")
    for linha, freq in linhas_mais_frequentes():
        st.write(f"{linha}: {freq}x")
    st.markdown("**Colunas Mais Frequentes:**")
    for col, freq in colunas_mais_frequentes():
        st.write(f"{col}: {freq}x")

with abas[3]:
    for (p, i), freq in pares_impares(jogos):
        st.write(f"{p} pares / {i} ímpares: {freq}x")

with abas[4]:
    for faixa, freq in soma_das_dezenas(jogos):
        st.write(f"Soma na faixa {faixa}-{faixa+9}: {freq}x")

with abas[5]:
    for quad, freq in quadrantes(jogos):
        st.write(f"Quadrante {quad}: {freq} dezenas")

with abas[6]:
    st.markdown("**Sequências Comuns:**")
    for seq, freq in sequencias_comuns(jogos):
        st.write(f"{seq}: {freq}x")
    st.markdown("**Duplas Comuns:**")
    for dupla, freq in duplas_mais_comuns(jogos):
        st.write(f"{dupla}: {freq}x")

with abas[7]:
    for rep, freq in repeticoes_com_concursos(jogos):
        st.write(f"{rep} dezenas repetidas: {freq}x")

with abas[8]:
    st.write("Dezenas que não saíram nos últimos concursos:")
    atras = dezenas_atrasadas(jogos)
    st.write(", ".join(f"{d:02}" for d in atras))

with abas[9]:
    for qtd, freq in quantidade_primos(jogos):
        st.write(f"{qtd} primos: {freq}x")

with abas[10]:
    for concurso, _, dezenas in jogos:
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

st.markdown("---")
st.markdown("<p style='text-align: center;'>Desenvolvido por <strong>SAMUCJ TECHNOLOGY</strong> 💡</p>", unsafe_allow_html=True)
