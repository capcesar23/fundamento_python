'''
    Comando for
    Comando while
    Comando range - para gerar números sequências
'''
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d)/4
print(f'A média é: {media}')

# nota = int(input('Entre com a nota'))
# while nota > 10: 
#     nota = int(input('Nota inválida. Entre com a nota correta: '))
#     print(nota)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)        


# div = 0
# a = int(input('Entre com o número: '))
# for x in range(1, a+1):
#     resto = a % x
#     print(a, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print(f'Número {a} é primo')
# else:
#     print(f'Número {a} não é primo')

# for x in range(100): # vai do 0 até 99
#    print(x)