import time


def slowprint(texto, atraso=0):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(atraso)

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/___
*******************************************************************************
''')

slowprint('VOCÊ ACORDA EM UMA PRAIA DESERTA, A DOR NA NUCA É IRRITANTE E FORTE, COMO SE ALGUÉM TIVESSE BATIDO NELA POUCAS'
      'HORAS ANTES. \n')
slowprint('VOCÊ LEVANTA, O CALOR E O VENTO QUENTE AUMENTAM A SENSAÇÃO DE MAL ESTAR, A CABEÇA AINDA ESTÁ ZONZA, UM FLASH '
      'DE MEMÓRIA PASSA EM SUA CABEÇA: "O CAPITÃO JHONY SPADER HAVIA LHE DADO UMA MISSÃO, QUE VOCÊ DEVERIA CUMPRIR POR'
      'LIVRE E ESPONTÂNEA PRESSÃO, CASO CONTRÁRIO A SUA LINDA E AMADA NOIVA KHATRINE BULOVA SERIA JOGADA AOS TUBARÕES. ')
slowprint('A AREIA DA PRAIA É BRANCA E FINA, TÃO FINA QUE QUANDO TENTA LAVAR PARTES DO CORPO NA AGUA A SENSAÇÃO DE AINDA TER AREIA'
      'ENTRE OS VÃOS DOS DEDOS É GRANDE, VOCÊ ESQUECE A IDEIA DE SE LIMPAR DA AREIA E OLHA EM VOLTA, PROCURANDO LUGARES '
      'ALTOS PARA OBSERVAR O TERRENO, E NOTA UM MORRO ALTO O SUFICIENTE PARA CHEGAR ANTES QUE ANOITEÇA, VOCÊ TAMBÉM PERCEBE'
      'QUE A FACHA DE AREIA É LARGA, PORÉM ASSIM QUE A PRAIA TERMINA, UMA SELVA DENSA COMEÇA. ')
slowprint('VOCÊ VASCULHA O BOLSO E ENCONTRA ANZOL LINHA DE PESCA E UM MAPA QUE NÃO MOSTRA A LOCALIZACAO DO TESOURO'
      'A UNICA COISA QUE VOCE SABE É QUE FOI ESCONDIDO EM UMA CAVERNA. OLHANDO PARA O MAPA É POSSÍVEL IDENTIFICAR QUE VOCE ESTÁ '
      'EM UMA ILHA. VOCÊ FAZ UMA PESCA ANTES DA JORNADA PARA SE ALIMENTAR E GUARDA ALGUNS PEIXES PARA O JANTAR.')
slowprint('AGORA QUE TEM UM MAPA VOCÊ DESISTE DA IDEIA DE SUBIR O MORRO E PARTE PARA A FLORESTA EM BUSCA DE CAVERNAS E GRUTAS'
      'NA PRIMEIRA QUE ENCONTRA, DENTRO DELA, UM BANDO DE MORCEGOS DORMEM, E VOCÊ PASSA SORRATEIRAMENTE, O MAPA NAO CONTEM'
      'INFORMAÇÕES DOS INTERIORES DA CAVERNA. VOCÊ RETIRA UMA PARTE DA ROUPA E ENROLA EM UM PEDAÇO DE MADEIRA QUE ENCONTRA.'
      '"OS ANOS NA MARINHA BRITÂNICA ME SERVIRAM DE ALGUMA COISA" COMENTA CONSIGO MESMO. EM ALGUNS INSTANTES VOCÊ TEM UMA TOCHA NAS MÃOS.')

choice1 = input('AO CAMINHAR DENTRO DA CAVERNA VOCÊ CHEGA EM UMA BIFURCAÇÃO, ONDE VOCÊ QUER IR? ESQUERDA OU DIREITA?\n').lower()
''
if choice1 == 'esquerda':
    print('VOCÊ CAMINHA POR ALGUNS MINUTOS, E LOGO ENCONTRA UMA AREA VASTA DEBAIXO DA MONTANHA, "UM LAGO DENTRO DE UMA CAVERNA!", '
          'O PENSAMETO ESCAPA DE DENTRO DE VOCÊ. AO APROXIMAR A TOCHA DA ÁGUA VOCÊ PERCEBE QUE A AGUA É CRISTALINA E '
          'É POSSÍVEL VER ALGUMAS MOEDAS DE PRATA DENTRO DA ÁGUA, PORÉM É FUNDO O SUFICIENTE PARA QUE NÃO ALCANCE '
          'OS PÉS NO CHÃO E PASSE ANDANDO. VOCÊ NOTA SINAIS DE EMBARCAÇÃO, E UM CAMINHO AO FUNDO, COMO SE PASSASSEM CANOAS POR ALI.')
    choice2 = input('O QUE VOCÊ QUER FAZER? NADAR ATÉ O OUTRO LADO OU ESPERAR POR UMA CANOA? \n').lower()
    if choice2 == 'esperar':
        print('VOCE ESPERA, E DEPOIS DE ALGUM TEMPO, UMA CANOA APARECE AO LONGE DO LAGO, UMA PEQUENA LAMPARINA NA FRENTE'
              'DA CANOA E ALGUEM EM PÉ COM UM GRANDE BASTÃO GUIANDO A EMBARCAÇÃO. QUANDO A CANOA SE APROXIMA VOCE ACENA'
              'E BALANÇA A TOCHA COMO UM SINAL DE QUE PRECISA DE UMA CARONA ATÉ O OUTRO LADO. A EMBARCAÇÃO VIRA EM SUA DIREÇÃO'
              'E SEGUE ATÉ QUE VOCÊ CONSIGA ALCANÇA-LA, O SENHOR GENTILMENTE LHE OFERECE CARONA POR ALGUMAS MOEDAS DE PRATA'
              'POREM VOCE NAO AS TEM. MAS PROMETE DIVIDIR O TESOURO CASO O ENCONTRE, O SENHOR DECIDE AJUDAR E VOCE EMBARCA.')
        print('APOS ALGUM TEMPO NAVEGANDO, VOCE AVISTA UM LOCAL DE SUBIDA ONDE APARENTEMENTE MUITOS TENTARAM SUBIR, POIS EXISTEM'
              'ESQUELETOS NA PARTE DE BAIXO DA SUBIDA, VOCE DECIDE QUE QUER VER O QUE HÁ NESTE LOCAL E PEDE PARA QUE O SENHOR'
              'GUIE A CANOA O MAIS PROXIMO POSSIVEL. AO ENCOSTAR VOCE SALTA E CONSEGUE SE AGARRAR A PARTE SUPERIOR, A ESCALADA É'
              'DIFÍCIL MAS VOCÊ CONSEGUE, E PERCEBE QUE EXISTE UM TÚNEL ILUMINADO POR RAIOS DE SOL QUE CONSEGUE TRANPASSAR POR ALGUMAS FRESTAS.'
              'AO FINAL DO TÚNEL EXISTEM 3 PORTAS DE TRES CORES DIFERENTES E VOCE PRECISA ESCOLHER UMA: ')
        choice3 = input('QUAL PORTA VOCÊ QUER ABRIR? VERMELHO, AZUL ou AMARELO?\n').lower()
        if choice3 == 'amarelo':
            print('PARABENS VOCE ENCONTROU O TESOURO PERDIDO, PAGOU UMA PARTE AO SENHOR E VOLTOU AO CAPITÃO JHONY SPADER E SALVOU A SUA AMADA!')
        elif choice3 == 'vermelho':
            print('game over')
        else:
            print('game over')
    else:
        print('VOCÊ TENTA NADAR MAS NÃO CONTAVA QUE ESTE LAGO ESTARIA INFESTADO DE CROCODILOS, '
              'OS ANIMAIS TE ABOCANHAM ARRANCANDO OS SEUS MEMBROS MANCHANDO A ÁGUA CRISTALINA DO LAGO COM O SEU '
              'GAME-OVER!')
        print(''' 
*******************************************************************************
                            _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
*******************************************************************************
                     ''')
else:
    print('game over')

