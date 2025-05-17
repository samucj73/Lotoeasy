from collections import Counter

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
