
import random
import sys
#Operadores aritméticos
a = 15
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
restoDivisao = a % b

print("Soma: ", soma)
print("Subtração ", subtracao)
print("multiplicação ", multiplicacao)
print("Divisão: ", divisao)
print("Resto da divisao: ", restoDivisao)

#Operador aritmetico composto
c = 2
c += 5
print("Valor de 'c' após o incremento: ", c)

d = 22
d **= 2 
print("Valor de 'd' após exponenciação: ", d)

#Maior e menor potencia
maiorPotencia = sys.float_info.max_10_exp
menorPotencia = sys.float_info.min_10_exp
print("A maior potência representada por 2: ", maiorPotencia)
print("A menor potência representada por 2: ", menorPotencia)

# Variáveis numéricas são imutáveis
x = 5
print("Antes da alteração:", x)
# Tentativa de alteração gera um erro
# x[0] = 2  # Isso causará um erro


#Métodos disponivéis para variáveis de ponto flutuante
numero = 7.85
print(numero.is_integer())

ratio = numero.as_integer_ratio() #verifica se o numero é inteiro
print(f"Razão inteira: {ratio}")


