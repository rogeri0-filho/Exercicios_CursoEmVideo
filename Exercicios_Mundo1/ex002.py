valor = input('Insira um valor para saber seu tipo primitivo: ')

print('O valor inserido é: ', type(valor))
print('É um valor númerico? : ', valor.isnumeric())
print('É uma letra? ', valor.isalpha())
print('Está em maiusculo? ', valor.isupper())
print('Está em minusculo? ', valor.islower())
print('Está capitalizada? ', valor.istitle())
print('Pode ser impresso? ', valor.isprintable())
print('Contem espaços? ', valor.isspace())
print('Possui letras ou números? ', valor.isalnum())

