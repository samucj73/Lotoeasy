from collections import Counter

def conferir_cartoes(cartoes, ultimos_resultados, filtrar_bons=False, min_acertos_13_ou_mais=2):
    """
    Compara os cartões gerados com os últimos 25 concursos.

    Parâmetros:
    - cartoes: lista de listas (cada cartão com 15 dezenas)
    - ultimos_resultados: lista de tuplas (concurso, data, dezenas sorteadas)
    - filtrar_bons: se True, retorna também os cartões com bom desempenho
    - min_acertos_13_ou_mais: número mínimo de vezes que um cartão precisa ter feito 13+ acertos

    Retorna:
    - resultados: lista de tuplas (concurso, acertos_por_cartao)
    - faixa_acertos: contagem geral de acertos entre 11 e 15
    - desempenho_cartoes: lista com quantidade de vezes que cada cartão teve 13+ acertos
    - bons_cartoes (se filtrar_bons=True): lista com apenas os cartões com desempenho satisfatório
    """
    resultados = []
    faixa_acertos = Counter()
    desempenho_cartoes = [0] * len(cartoes)  # índice → qtd de vezes com 13+

    for concurso, data, dezenas_sorteadas in ultimos_resultados:
        acertos_por_cartao = []
        sorteio = set(dezenas_sorteadas)
        for i, cartao in enumerate(cartoes):
            acertos = len(set(cartao) & sorteio)
            acertos_por_cartao.append(acertos)
            if 11 <= acertos <= 15:
                faixa_acertos[acertos] += 1
            if acertos >= 13:
                desempenho_cartoes[i] += 1
        resultados.append((concurso, acertos_por_cartao))

    bons_cartoes = []
    if filtrar_bons:
        bons_cartoes = [cartoes[i] for i, vezes in enumerate(desempenho_cartoes) if vezes >= min_acertos_13_ou_mais]

    if filtrar_bons:
        return resultados, faixa_acertos, desempenho_cartoes, bons_cartoes
    else:
        return resultados, faixa_acertos, desempenho_cartoes
