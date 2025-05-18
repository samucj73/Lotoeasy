from collections import Counter
import streamlit as st

def conferir_cartoes(cartoes, ultimos_resultados):
    """
    Compara os cartões gerados com os últimos 25 concursos.
    
    Parâmetros:
    - cartoes: lista de listas (cada cartão com 15 dezenas)
    - ultimos_resultados: lista de tuplas (concurso, data, dezenas sorteadas)

    Retorna:
    - lista de tuplas: (concurso, acertos_por_cartao)
    - contagem de acertos por faixa (Counter)
    """
    resultados = []
    faixa_acertos = Counter()

    for concurso, data, dezenas_sorteadas in ultimos_resultados:
        acertos_por_cartao = []
        sorteio = set(dezenas_sorteadas)
        for cartao in cartoes:
            acertos = len(set(cartao) & sorteio)
            acertos_por_cartao.append(acertos)
            if 11 <= acertos <= 15:
                faixa_acertos[acertos] += 1
        resultados.append((concurso, acertos_por_cartao))
    
    return resultados, faixa_acertos


def conferir_mais_recente(cartoes, ultimos_resultados, qtd_cartoes):
    faixa_acertos = Counter()
    acertos_por_cartao = []

    if not ultimos_resultados:
        return None, [], Counter()

    concurso, data, dezenas_sorteadas = ultimos_resultados[-1]
    sorteio = set(dezenas_sorteadas)

    for cartao in cartoes[:qtd_cartoes]:
        acertos = len(set(cartao) & sorteio)
        acertos_por_cartao.append(acertos)
        if 11 <= acertos <= 15:
            faixa_acertos[acertos] += 1

    return (concurso, data, dezenas_sorteadas), acertos_por_cartao, faixa_acertos


# ----------- Trecho Streamlit que você deve colocar na aba onde quer conferir -----------

# Exemplo de variáveis que devem estar definidas no seu app:
# cartoes_gerados = [...]  # lista dos cartões gerados
# ultimos_resultados = [...]  # lista dos últimos resultados (tuplas com concurso, data, dezenas)

qtd_cartoes = st.slider("Quantos cartões deseja conferir?", 1, 100, 10)

if st.button("Conferir agora"):
    resultado, acertos, faixas = conferir_mais_recente(cartoes_gerados, ultimos_resultados, qtd_cartoes)

    if resultado:
        concurso, data, dezenas = resultado

        st.subheader(f"Concurso {concurso} - {data}")
        st.write(f"Dezenas sorteadas: {sorted(dezenas)}")

        st.subheader("Resultado por Cartão:")
        for i, qtd_acertos in enumerate(acertos, 1):
            st.write(f"Cartão {i}: {qtd_acertos} acertos")

        st.subheader("Resumo das Faixas de Acerto:")
        for pontos in range(15, 10, -1):
            st.write(f"{pontos} pontos: {faixas.get(pontos, 0)}")
    else:
        st.warning("Nenhum sorteio disponível para conferir.")
