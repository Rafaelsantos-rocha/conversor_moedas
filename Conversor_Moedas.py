#conversor de unidades monetárias

import sys
import os

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

real_dolar = 0.18 # 1 real
real_euro = 0.19 # 1 real
real_btcoin = 0.0000100 # 1 real
dolar_real = 5.36 # 1 dolar
dolar_euro = 1.03 # 1 dolar
dolar_btcoin = 0.000052 # 1 dolar
euro_real = 5.16 # 1 euro
euro_dolar = 0.96 # 1 euro
euro_btcoin = 0.000052 # 1 euro
btcoin_real = 100409.05 # 1 bitcoin
btcoin_dolar = 19287.00 # 1 bitcoin
btcoin_euro = 19668.59 # 1bitcoin 

real = 1
dolar = 2
euro = 3
bitcoin = 4

print('\n## CONVERSOR DE UNIDADES MONETÁRIAS ##')
print('\nOBSERVAÇÃO DE USO: UTILIZE SEMPRE O "." CASO SEJA NECESSÁRIO ACRESCENTAR UM VALOR DECIMAL( O MESMO VALE PARA BITCOIN ) EX:\n5.52 OU 0.05\n')

while True:
 try:
  unidade1 = int(input('\nEscolha a opção monetária que você deseja converter: \n1 real \n2 dolar \n3 euro \n4 Bitcoin \n'))
  if unidade1 > 0 and unidade1 <= 4:
   valor = float(input('\nDigite o valor a ser convertido: $'))
   conversão1 =  valor*0.18 # real_dolar
   conversão2 =  valor*0.19 # real_euro
   conversão3 =  valor*0.0000100 # real_bitcoin
   conversão4 =  valor*5.36 # dolar_real
   conversão5 =  valor*1.03 # dolar_euro
   conversão6 =  valor*0.000052 # dolar_bitcoin
   conversão7 =  valor*5.16 # euro_real
   conversão8 =  valor*0.96 # euro_dolar
   conversão9 =  valor*0.000052 # euro_bitcoin
   conversão10 =  valor*100409.05 # bitcoin_real
   conversão11 =  valor*19287.00 # bitcoin_dolar
   conversão12 =  valor*19668.59 # bitcoin_euro
   break
  else:
   print ('\nOpção invalida! Favor escolher entre as opções 1 a 4!')
   unidade1 = float(input('\nEscolha a opção monetária que você deseja converter: \n1 real \n2 dolar \n3 euro \n4 Bitcoin \n'))
 except ValueError:
   print('\nDigite apenas números!')

while True:
  try:
   unidade2 = int(input('\nEscolha a opção monetária a qual o valor sera convertido:  \n1 real \n2 dolar \n3 euro \n4 Bitcoin \n'))
   if unidade2 > 0 and unidade2 <= 4:
    print ('\nConfira abaixo o resultado da conversão!\n')
    break
   else:
    print ('\nOpção invalida! Favor escolher entre as opções 1 a 4!')
    unidade2 = int(input('\nEscolha a opção monetária a qual o valor sera convertido:  \n1 real \n2 dolar \n3 euro \n4 Bitcoin \n'))
  except ValueError:
   print('\nDigite apenas números!') 

if unidade1 == unidade2:
   if unidade1 and unidade2 == 1:
    print(f'Não é possivel converter Real para Real!')
   elif unidade1 and unidade2 == 2:
    print(f'Não é possivel converter Dolar para Dolar!')
   elif unidade1 and unidade2 == 3:
    print(f'Não é possivel converter Euro para Euro!')
   elif unidade1 and unidade2 == 4:
    print(f'Não é possivel converter Bitcoin para Bitcoin!')

elif unidade1 == real and unidade2 == dolar:
   print(f'Você converteu real para dolar: ', conversão1,'$')
elif unidade1 == real and unidade2 == euro:
   print(f'Você converteu real para euro: ', conversão2,'$')
elif unidade1 == real and unidade2 == bitcoin:
   print(f'Você converteu real para bitcoin: ', conversão3,'BTC')
elif unidade1 == dolar and unidade2 == real:
   print(f'Você converteu dolar para real: ', conversão4,'$')
elif unidade1 == dolar and unidade2 == euro:
   print(f'Você converteu dolar para euro: ', conversão5,'$')
elif unidade1 == dolar and unidade2 == bitcoin:
   print(f'Você converteu dolar para bitcoin: ', conversão6,'BTC')
elif unidade1 == euro and unidade2 == real:
   print(f'Você converteu euro para real: ', conversão7,'$')
elif unidade1 == euro and unidade2 == dolar:
   print(f'Você converteu euro para dolar: ', conversão8,'$')
elif unidade1 == euro and unidade2 == bitcoin:
   print(f'Você converteu euro para bitcoin: ', conversão9,'BTC')
elif unidade1 == bitcoin and unidade2 == real:
   print(f'Você converteu bitcoin para real: ', conversão10,'$')
elif unidade1 == bitcoin and unidade2 == dolar:
   print(f'Você converteu bitcoin para dolar: ', conversão11,'$')
elif unidade1 == bitcoin and unidade2 == euro:
   print(f'Você converteu bitcoin para euro:', conversão12,'$')

reset = int(input('\nDeseja realizar nova consulta? \n1 - SIM \n2 - NÃO \n'))
while True:
 if int(reset) == 1:
  print('\nPrograma será reinicializado\n')
  restart_program()
 elif int(reset) == 2:
  print('\nPrograma será finalizado.\n')
  sys.exit
 break