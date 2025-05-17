# analise_avancada.py
from collections import Counter

def analise_gaps(jogos):
    contador = Counter()
    for _, _, dezenas in jogos:
        dezenas = sorted(dezenas)
        gaps = [dezenas[i+1] - dezenas[i] for i in range(len(dezenas) - 1)]
        for gap in gaps:
            contador[gap] += 1
    return sorted(contador.items())

def soma_extremos(jogos):
    contador = Counter()
    for _, _, dezenas in jogos:
        menor = min(dezenas)
        maior = max(dezenas)
        soma = menor + maior
        contador[soma] += 1
    return sorted(contador.items(), key=lambda x: -x[1])

def media_das_dezenas(jogos):
    medias = Counter()
    for _, _, dezenas in jogos:
        media = round(sum(dezenas) / len(dezenas), 2)
        medias[media] += 1
    return sorted(medias.items(), key=lambda x: -x[1])

def digitos_finais(jogos):
    finais = Counter()
    for _, _, dezenas in jogos:
        for d in dezenas:
            finais[d % 10] += 1
    return sorted(finais.items())

def digitos_iniciais(jogos):
    iniciais = Counter()
    for _, _, dezenas in jogos:
        for d in dezenas:
            inicial = int(str(d)[0])
            iniciais[inicial] += 1
    return sorted(iniciais.items())

def dezenas_menos_correlacionadas(jogos, limite=20):
    total_jogos = len(jogos)
    pares = Counter()
    ocorrencias = Counter()

    for _, _, dezenas in jogos:
        for dez in dezenas:
            ocorrencias[dez] += 1
        for i in range(len(dezenas)):
            for j in range(i+1, len(dezenas)):
                par = tuple(sorted((dezenas[i], dezenas[j])))
                pares[par] += 1

    resultados = []
    for (d1, d2), freq in pares.items():
        total_d1_d2 = min(ocorrencias[d1], ocorrencias[d2])
        if total_d1_d2 > 0:
            percentual = freq / total_d1_d2
            resultados.append(((d1, d2), percentual))

    resultados.sort(key=lambda x: x[1])
    return resultados[:limite]

def distancia_entre_aparicoes(jogos):
    ultima_aparicao = {d: -1 for d in range(1, 26)}
    distancias = {d: [] for d in range(1, 26)}

    for idx, (_, _, dezenas) in enumerate(jogos):
        for d in range(1, 26):
            if d in dezenas:
                if ultima_aparicao[d] != -1:
                    distancias[d].append(idx - ultima_aparicao[d])
                ultima_aparicao[d] = idx
    return {d: distancias[d] for d in distancias if distancias[d]}
