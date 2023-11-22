import random
#Operadores aritmeticos simples
num1 = 5 + 6
print ("A soma é: ", num1)
num2 = 54 - 38
print ("A subtracao é: ", num2)
num3 = 25 * 40
print ("A multiplicacao é: ", num3)
#Operadores aritmeticos composto
bala = 15
bala = bala + 3
bala += 2
bala -= 5
print ("Operador composto: ", bala)
#Diferença em relaçao a C++
print ("A divisao é: ", (25 // 5))
#Calculando fatorial
num5 = 5**30
print ("O fatorial de 30 é: ", num5)

#exemplo de imutabilidade de variáveis numéricas
x = 10
print("Valor inicial de x: ", x)
# Tentativa de modificar diretamente a variável
# Isso resultará em um erro
# x += 5  # Descomente esta linha para ver o erro

#Criando uma nova variável com o valor modificado 
y = x + 7
print ("Novo valor de x: ", y)

#Alguns métodos disponíveis para variáveis inteiras
a = 15
a_str = str(a)
a_float = float(a)
a_abs = abs(a)

# Método para verificar se o número é par
is_even = a % 2 == 0
print("É par?", is_even)






