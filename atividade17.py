# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.
ano = int(input( " Digite o Ano: "))
if ano % 100 !=0 and ano % 4 ==0 or ano % 400 ==0 :
    print(" Este Ano é Bissexto ")

else:
    print(" Este Ano não é Bissexto")