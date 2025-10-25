def define_posicoes(linha, coluna, orientacao, tamanho):
    listafinal = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            listafinal.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            listafinal.append([linha, coluna + i])
    return listafinal


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    navio_posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = [navio_posicao]
    else:
        frota[nome_navio].append(navio_posicao)
    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro


def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for i in range(10)]

    for tipo in frota:
        for unidade in frota[tipo]:
            for i in range(10):
                for j in range(10):
                    if [i, j] in unidade:
                        tabuleiro[i][j] = 1
    return tabuleiro


def afundados(frota, tabuleiro):
    quantos_afundados = 0
    for tipo in frota:
        for navio in frota[tipo]:
            afundado = True
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] == 1:
                    afundado = False
                    continue
            if afundado:
                quantos_afundados += 1
    return quantos_afundados


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    navionovo = define_posicoes(linha, coluna, orientacao, tamanho)
    for i in range(len(navionovo)):
        if navionovo[i][0] > 9 or navionovo[i][1] > 9:
            return False
    for i in range(len(navionovo)):
        for tipo in frota:
            for j in range(len(frota[tipo])):
                for k in range(len(frota[tipo][j])):
                    if frota[tipo][j][k] == navionovo[i]:
                        return False
    return True
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto