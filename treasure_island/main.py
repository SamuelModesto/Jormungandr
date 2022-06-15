import time


def slowprint(texto, atraso=0.05direi):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(atraso)



print('''              ,.  _~-.,                .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^''')

slowprint(
    'VOCÊ ACORDA EM UMA PRAIA DESERTA, A DOR NA NUCA É IRRITANTE E FORTE, COMO SE ALGUÉM TIVESSE BATIDO NELA POUCAS'
    'HORAS ANTES. \n'
    'VOCÊ LEVANTA, O CALOR E O VENTO QUENTE AUMENTAM A SENSAÇÃO DE MAL ESTAR, A CABEÇA AINDA ESTÁ ZONZA, UM FLASH '
    'DE MEMÓRIA PASSA EM SUA CABEÇA: \n"O CAPITÃO JHONY SPADER HAVIA LHE DADO UMA MISSÃO, QUE VOCÊ DEVERIA CUMPRIR POR'
    'LIVRE E ESPONTÂNEA PRESSÃO, CASO CONTRÁRIO \nA SUA LINDA E AMADA NOIVA KHATRINE BULOVA SERIA JOGADA AOS TUBARÕES. \n'
    'A AREIA DA PRAIA É BRANCA E FINA, TÃO FINA QUE QUANDO TENTA LAVAR PARTES DO CORPO NA AGUA A SENSAÇÃO DE AINDA TER AREIA'
    'ENTRE OS VÃOS DOS DEDOS É GRANDE, \nVOCÊ ESQUECE A IDEIA DE SE LIMPAR DA AREIA E OLHA EM VOLTA, PROCURANDO LUGARES '
    'ALTOS PARA OBSERVAR O TERRENO, E NOTA UM MORRO ALTO O SUFICIENTE PARA \nCHEGAR ANTES QUE ANOITEÇA, VOCÊ TAMBÉM PERCEBE '
    'QUE A FACHA DE AREIA É LARGA, PORÉM ASSIM QUE A PRAIA TERMINA, UMA SELVA DENSA COMEÇA. '
    '\nVOCÊ VASCULHA O BOLSO E ENCONTRA ANZOL LINHA DE PESCA E UM MAPA QUE NÃO MOSTRA A LOCALIZACAO DO TESOURO'
    'A UNICA COISA QUE VOCE SABE É QUE FOI ESCONDIDO \nEM UMA CAVERNA. OLHANDO PARA O MAPA É POSSÍVEL IDENTIFICAR QUE VOCE ESTÁ '
    'EM UMA ILHA, VOCÊ FAZ UMA PESCA ANTES DA JORNADA PARA SE ALIMENTAR E GUARDA \nALGUNS PEIXES PARA O JANTAR. '
    'AGORA QUE TEM UM MAPA VOCÊ DESISTE DA IDEIA DE SUBIR O MORRO E PARTE PARA A FLORESTA EM BUSCA DE CAVERNAS E GRUTAS. '
    '\nNA PRIMEIRA QUE ENCONTRA, DENTRO DELA, UM BANDO DE MORCEGOS DORMEM, E VOCÊ PASSA SORRATEIRAMENTE, O MAPA NAO CONTEM '
    'INFORMAÇÕES DOS INTERIORES \nDAS CAVERNAS. VOCÊ RETIRA UMA PARTE DA ROUPA E ENROLA EM UM PEDAÇO DE MADEIRA QUE ENCONTRA.'
    '"OS ANOS NA MARINHA BRITÂNICA ME SERVIRAM DE ALGUMA COISA." \nCOMENTA CONSIGO MESMO. EM ALGUNS INSTANTES VOCÊ TEM UMA TOCHA NAS MÃOS.\n')

choice1 = input(slowprint('AO CAMINHAR DENTRO DA CAVERNA VOCÊ CHEGA EM UMA BIFURCAÇÃO, ONDE VOCÊ QUER IR? ESQUERDA OU DIREITA?')).lower()
if choice1 == 'esquerda':
    print(''' 
     **********************************************************************************************                                 
       ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
       ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
        ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
        ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
        ~~~~ ~ ~======~~  ~~ ~ ~~~~~~ ~~~~~  ~~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
        ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
       ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
        ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
        ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~
        ~~~~ ~ ~======~~  ~~ ~ ~~~~~~ ~~~~~  ~~~ ~ ~~~~ ~ ~======~~  ~~ ~ ~~~~ ~ ~======~~  ~~ ~ 
    ***********************************************************************************************   
        ''')
    slowprint(
        'VOCÊ CAMINHA POR ALGUNS MINUTOS, E LOGO ENCONTRA UMA AREA VASTA DEBAIXO DA MONTANHA, "UM LAGO DENTRO DE UMA CAVERNA!", '
        'O PENSAMETO ESCAPA DE DENTRO \nDE VOCÊ. AO APROXIMAR A TOCHA DA ÁGUA VOCÊ PERCEBE QUE A AGUA É CRISTALINA  E '
        'É POSSÍVEL VER ALGUMAS MOEDAS DE PRATA DENTRO DA ÁGUA, PORÉM É FUNDO \nO SUFICIENTE PARA QUE NÃO ALCANCE '
        'OS PÉS NO CHÃO E PASSE ANDANDO. \nVOCÊ NOTA SINAIS DE EMBARCAÇÃO, E UM CAMINHO AO FUNDO, COMO SE PASSASSEM CANOAS POR ALI.\n')
    choice2 = input(slowprint('O QUE VOCÊ QUER FAZER? NADAR ATÉ O OUTRO LADO OU ESPERAR POR UMA CANOA? \n')).lower()
    if choice2 == 'esperar':
        print('''
                                         __________/\__________
             ~~~~~~ ~======~~  ~~~~~~ ~~~\____________________/~~~~~~ ~======~~  ~~ ~ 
             ~~~~~ ~======~~  ~~~~~ ~ ~~~ ~~~. ~  ~~~~~~ ~======~~  ~~ ~ ~~~~ ~ ~=====
        *******************************************************************************
        ''')
        slowprint(
            'VOCE ESPERA, E DEPOIS DE ALGUM TEMPO, UMA CANOA APARECE AO LONGE DO LAGO, UMA PEQUENA LAMPARINA NA FRENTE ' 
            'DA CANOA E ALGUEM EM PÉ \nCOM UM GRANDE BASTÃO GUIANDO A EMBARCAÇÃO. \nQUANDO A CANOA SE APROXIMA VOCE ACENA '
            'E BALANÇA A TOCHA COMO UM SINAL DE QUE PRECISA DE UMA CARONA ATÉ O OUTRO LADO. \nA EMBARCAÇÃO VIRA EM SUA DIREÇÃO '
            'E SEGUE ATÉ QUE VOCÊ CONSIGA ALCANÇA-LA, O SENHOR GENTILMENTE LHE OFERECE CARONA POR \nALGUMAS MOEDAS DE PRATA '
            'POREM VOCE NAO AS TEM. \nMAS PROMETE DIVIDIR O TESOURO CASO O ENCONTRE, O SENHOR DECIDE AJUDAR E VOCE EMBARCA. \n'
            'APOS ALGUM TEMPO NAVEGANDO, VOCE AVISTA UM LOCAL DE SUBIDA ONDE APARENTEMENTE MUITOS TENTARAM SUBIR, POIS EXISTEM '
            'ESQUELETOS NA PARTE DE BAIXO DA SUBIDA.\n VOCE DECIDE QUE QUER VER O QUE HÁ NESTE LOCAL E PEDE PARA QUE O SENHOR '
            'GUIE A CANOA O MAIS PROXIMO POSSIVEL. \nAO ENCOSTAR VOCE SALTA E CONSEGUEM SE AGARRAR A PARTE SUPERIOR, A ESCALADA É'
            'DIFÍCIL MAS VOCÊ CONSEGUE, E PERCEBE QUE EXISTE UM TÚNEL \nILUMINADO POR RAIOS DE SOL QUE CONSEGUE TRANPASSAR POR ALGUMAS FRESTAS. \n'
            'AO FINAL DO TÚNEL EXISTEM 3 PORTAS DE TRES CORES DIFERENTES E VOCE PRECISA ESCOLHER UMA...\n')
        choice3 = input('QUAL PORTA VOCÊ QUER ABRIR? VERMELHO, AZUL ou AMARELO?\n').lower()
        if choice3 == 'amarelo':
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
            slowprint('PARABENS VOCE ENCONTROU O TESOURO PERDIDO, \nPAGOU UMA PARTE AO SENHOR E VOLTOU AO CAPITÃO '
                      'JHONY SPADER E SALVOU A SUA AMADA!')
        elif choice3 == 'vermelho':
            print('''
         *******************************************************************************   
                                               ____                      ,
                                  /---.'.__             ____//
                                       '--.\           /.---'
                                  _______  \\         //
                                /.------.\  \|      .'/  ______
                               //  ___  \ \ ||/|\  //  _/_----.\__
                              |/  /.-.\  \ \:|< >|// _/.'..\   '--'
                                 //   \'. | \'.|.'/ /_/ /  \\
                                //     \ \_\/" ' ~\-'.-'    \\
                               //       '-._| :H: |'-.__     \\
                              //           (/'==='\)'-._\     ||
                              ||                        \\    \|
                              ||                         \\    '
                              |/                          \\
                                                           ||
                                                           ||
                                                           \\
         *******************************************************************************      
            ''')
        else:
            print('''
        ******************************************************************************   
                                
                                   (  .      )
                               )           (              )
                                     .  '   .   '  .  '  .
                            (    , )       (.   )  (   ',    )
                             .' ) ( . )    ,  ( ,     )   ( .
                          ). , ( .   (  ) ( , ')  .' (  ,    )
                         (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ******************************************************************************   
            ''')
            slowprint('VOCE ABRE A PORTA E CHAMAS TE QUEIMAM, SEM DEIXAR NENHUMA CHANCE PARA SOBREVIVENCIA GAME-OVER!')
    else:
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
        slowprint('VOCÊ TENTA NADAR MAS NÃO CONTAVA QUE ESTE LAGO ESTARIA INFESTADO DE CROCODILOS, \n '
                  'OS ANIMAIS TE ABOCANHAM ARRANCANDO OS SEUS MEMBROS MANCHANDO A ÁGUA CRISTALINA DO LAGO COM O SEU SANGUE '
                  'GAME-OVER!')

else:
    print('''
     *******************************************************************************      
                         ________________________________         
                          /                                "-_          
                         /      .  |  .                       \          
                        /      : \ | / :                       \         
                       /        '-___-'                         \      
                      /_________________________________________ \      
                           _______| |________________________--""-L 
                          /       F J                              \ 
                         /       F   J                              L
                        /      :'     ':                            F
                       /        '-___-'                            / 
                      /_________________________________________--"  
   ***********************************************************************************
 ''')
    slowprint('VOCE CAMINHA E MESMO COM A TOCHA NAO PERCEBE UM BURACO NA SUA FRENTE, \n ESCORREGA E CAI EM UM BURACO PROFUNDO '
              'SEM CHANCE DE ESCAPATÓRIA OU SOBREVIVÊNCIA GAME-OVER!')
