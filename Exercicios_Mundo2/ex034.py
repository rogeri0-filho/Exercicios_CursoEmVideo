from time import sleep

print('~' * 26)
print('   EMPRÉSTIMO BANCÁRIO!')
print('~' * 26)

sleep(2)
print('O empréstimo bancário não pode exceder 30% do seu salário!')
sleep(1)

casa = float(input('Qual o valor da casa que você deseja comprar: R$'))
salário = float(input('Qual o seu salário: R$'))

ano = int(input('Em quantos anos deseja pagar? '))

prestação = (casa / (ano * 12))
excedente = (salário * (30/100))

sleep(3)

if prestação > excedente:
    print(f'Para pagar uma casa de R${casa:.2f} em {ano} anos, sua prestação seria de R${prestação:.2f}.')
    print('A prestação excede os 30% permitidos do seu salário...')
    print('Seu empréstimo foi negado!')
else:
    print('A prestação não excede os 30% permitidos do seu salário!')
    print('Seu empréstimo foi aprovado!')
 
