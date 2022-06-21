import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
escolhas = [rock, paper, scissors]

escolha_usuario = int(input('Qual a sua escolha? digite 0 para pedra, 1 para papel e 2 para tesoura: '))
print(escolhas[escolha_usuario])

print('Escolha do computador: ')
escolha_computador = random.randint(0, 2)
print(escolhas[escolha_computador])

msg_venceu = 'You win'
msg_perdeu = 'You lose'

if escolha_usuario == 0 and escolha_computador == 1:
    print(msg_perdeu)
elif escolha_usuario == 0 and escolha_computador == 2:
    print(msg_venceu)
elif escolha_usuario == 1 and escolha_computador == 0:
    print(msg_venceu)
elif escolha_usuario == 1 and escolha_computador == 2:
    print(msg_perdeu)
elif escolha_usuario == 2 and escolha_computador == 0:
    print(msg_perdeu)
elif escolha_usuario == 2 and escolha_computador == 1:
    print(msg_venceu)
else:
    print('empate')



