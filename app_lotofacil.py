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
from analise_avancada import (
    analise_gaps,
    soma_extremos,
    media_das_dezenas,
    digitos_finais,
    digitos_iniciais,
    dezenas_menos_correlacionadas,
    distancia_entre_aparicoes
)
from util import exportar_txt, exportar_pdf
from gerador_lotofacil import gerar_cartoes_personalizados
from gerador_inteligente import gerar_cartoes_inteligentes
import io
from fpdf import FPDF

st.set_page_config(page_title="LotoFácil Inteligente", layout="wide")
st.markdown("<h1 style='text-align: center;'>🍀 LotoFácil Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Gere cartões com base em estatísticas reais e personalização</p>", unsafe_allow_html=True)

st.markdown("### 🎯 Geração de Cartões")
qtd_cartoes = st.slider("Quantos cartões deseja gerar?", 1, 500, 1)
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
        cartoes = gerar_cartoes_personalizados(qtd_cartoes, list(fixas or []), list(excluir or []))
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
    "Repetições", "Dezenas Atrasadas", "Números Primos",
    "Últimos Resultados", "Análises Avançadas", "Conferência de Cartões"
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

with abas[11]:
    st.markdown("### 🔍 Análises Avançadas dos Jogos")

    st.subheader("📏 Gaps entre Dezenas")
    for gap, freq in analise_gaps(jogos):
        st.write(f"Gap {gap}: {freq} ocorrência(s)")

    st.subheader("📐 Soma dos Extremos")
    for soma, freq in soma_extremos(jogos)[:10]:
        st.write(f"Soma {soma}: {freq} ocorrência(s)")

    st.subheader("📊 Média das Dezenas")
    for media, freq in media_das_dezenas(jogos)[:10]:
        st.write(f"Média {media}: {freq} ocorrência(s)")

    st.subheader("🔢 Dígitos Finais das Dezenas")
    finais = dict(digitos_finais(jogos))
    st.bar_chart(finais)

    st.subheader("🔠 Dígitos Iniciais das Dezenas")
    iniciais = dict(digitos_iniciais(jogos))
    st.bar_chart(iniciais)

    st.subheader("🚫 Dezenas Menos Correlacionadas")
    for dupla, perc in dezenas_menos_correlacionadas(jogos):
        st.write(f"{dupla}: {perc:.2%} de coocorrência")

    st.subheader("📅 Distância Entre Aparições")
    dists = distancia_entre_aparicoes(jogos)
    for dez, valores in dists.items():
        st.write(f"Dezena {dez:02}: {valores}")


# ... (demais imports permanecem iguais)

# Dentro da aba de conferência (abas[12]):
with abas[12]:
    st.markdown("### 📋 Conferência dos Cartões Gerados com os Últimos 25 Resultados")

    if 'cartoes' not in st.session_state:
        st.info("Gere os cartões primeiro para realizar a conferência.")
    else:
        cartoes = st.session_state['cartoes']
        ultimos = list(ultimos_resultados())
        resultados = [set(dezenas) for _, _, dezenas in ultimos]

        faixas = {15: 0, 14: 0, 13: 0, 12: 0, 11: 0}
        detalhes_cartoes = []

        for i, cartao in enumerate(cartoes, 1):
            melhor_acerto = 0
            melhor_concurso = ""
            for concurso, _, dezenas_sorteadas in ultimos:
                acertos = len(set(cartao) & set(dezenas_sorteadas))
                if acertos in faixas:
                    faixas[acertos] += 1
                if acertos > melhor_acerto:
                    melhor_acerto = acertos
                    melhor_concurso = concurso
            if melhor_acerto >= 13:
                detalhes_cartoes.append((i, melhor_acerto, melhor_concurso, cartao))

        st.subheader("🎯 Resultados da Conferência")
        for pontos in sorted(faixas.keys(), reverse=True):
            st.write(f"🟢 Cartões com {pontos} pontos: {faixas[pontos]}")

        st.subheader("📄 Cartões que acertaram (12+ pontos)")
        for i, pontos, concurso, cartao in detalhes_cartoes:
            st.markdown(
                f"- Cartão **{i:02}** → **{pontos} pontos** no concurso **{concurso}** → "
                + " ".join(f"{d:02}" for d in sorted(cartao))
            )




st.markdown("---")

# === Seção Exportação com download_button ===

def gerar_txt(cartoes):
    linhas = [f"Cartão {i}: {' - '.join(f'{n:02}' for n in sorted(c))}" for i, c in enumerate(cartoes, 1)]
    return "\n".join(linhas)

def gerar_pdf_bytes(cartoes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for i, c in enumerate(cartoes, 1):
        pdf.cell(0, 10, txt=f"Cartão {i}: {' - '.join(f'{n:02}' for n in sorted(c))}", ln=True)
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return pdf_bytes

st.subheader("📤 Exportar Cartões")

if st.session_state.get('cartoes'):
    cartoes = st.session_state['cartoes']

    txt_conteudo = gerar_txt(cartoes)
    pdf_bytes = gerar_pdf_bytes(cartoes)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <style>
            div.stDownloadButton > button:first-child {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                padding: 10px 24px;
                border-radius: 8px;
            }
            div.stDownloadButton > button:first-child:hover {
                background-color: #45a049;
            }
            </style>
            """, unsafe_allow_html=True)
        st.download_button(
            label="⬇️ Baixar Cartões (.TXT)",
            data=txt_conteudo,
            file_name="cartoes_lotofacil.txt",
            mime="text/plain",
        )
    with col2:
        st.markdown("""
            <style>
            div.stDownloadButton > button:first-child {
                background-color: #2196F3;
                color: white;
                font-size: 16px;
                padding: 10px 24px;
                border-radius: 8px;
            }
            div.stDownloadButton > button:first-child:hover {
                background-color: #0b7dda;
            }
            </style>
            """, unsafe_allow_html=True)
        st.download_button(
            label="⬇️ Baixar Cartões (.PDF)",
            data=pdf_bytes,
            file_name="cartoes_lotofacil.pdf",
            mime="application/pdf",
        )
else:
    st.info("Gere os cartões acima para habilitar a exportação.")

st.markdown("---")
st.markdown("<p style='text-align: center;'>Desenvolvido por <strong>SAMUCJ TECHNOLOGY</strong> 💡</p>", unsafe_allow_html=True)
