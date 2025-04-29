# Funções em python iniciam com a palavra 
# reservada def.
# funções são rotinas em seu conceito

# def saudacao():
#     print ('olá mundo!')

# saudacao()


# def mostrar_linha():
#     print(30* "=")

# mostrar_linha ()
# print('MODULO 01')
# mostrar_linha ()
# print('ALGORITMOS')
# mostrar_linha ()
# print('ANALISE DE DADOS')
# mostrar_linha ()


# def saudacao(nome):
#     print(f'ola {nome}!')

# nome = input ('informe o nome: ')
# # saudacao(nome)

# def somar(a,b):
#     somar = a + b
#     print(soma)
    #   return s



def somar_numeros(x,y):
     s = x + y
     return s

for i in range (3):
    n1 = int(input('Informe o número:'))
    n2 = int(input('Informe o número:'))

    soma = somar_numeros(n1, n2)
    print (soma)
