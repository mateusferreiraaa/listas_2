# Definição Variavis:
p_mes = int(input('Escolha um número de 1 a 12: '))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
if p_mes > 12:
    print('Número celecionado é imcompativel! Por favor escoloha um numero compatiivel!')
else:
    print(meses[p_mes - 1])