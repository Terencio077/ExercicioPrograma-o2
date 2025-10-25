from funcoes import define_posicoes, posicao_valida, preenche_frota
from funcoes import define_posicoes, posicao_valida, preenche_frota, posiciona_frota, monta_tabuleiros, afundados, faz_jogada

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
} 

navios = {
    "porta-aviões":[4],
    "navio-tanque":[3, 3],
    "contratorpedeiro":[2, 2, 2],
    "submarino": [1, 1, 1, 1],
}

for tipo in navios:
        for valor in navios[tipo]:
            tamanho = valor
            while True:
                print(f"Insira as informações referentes ao navio {tipo} que possui tamanho {tamanho}")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                if tipo != 'submarino':
                    orientacao = int(input("[1] Vertical [2] Horizontal >"))
                    if orientacao == 1:
                        orientacao = 'vertical'
                    elif orientacao == 2:
                        orientacao = 'horizontal'
                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    define_posicoes(linha, coluna, orientacao, tamanho)
                    preenche_frota(frota, tipo, linha, coluna, orientacao, tamanho)
                    break
                else: 
                    print("Esta posição não está válida!")
print(frota)
    

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
while True:
    linha = int(input('Jogador, qual linha deseja atacar? '))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Jogador, qual linha deseja atacar? '))
    coluna = int(input('Jogador, qual coluna deseja atacar? '))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
    if tabuleiro_oponente[linha][coluna] == '-' or tabuleiro_oponente[linha][coluna] == 'X':
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        continue
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))