##Faça um Programa que peça as 4 notas bimestrais e mostre a média.
B1 = float(input('Informe a nota do primeiro bimestre: '))
B2 = float(input('Informe a nota do segundo bimestre: '))
B3 = float(input('Informe a nota do terceiro bimestre: '))
B4 = float(input('Informe a nota do quarto bimestre: '))

medianual = (b1+b2+b3+b4)/4
print('A média anual foi de {}'.format(medianual))
