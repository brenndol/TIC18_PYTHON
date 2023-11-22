import random

def imprimir_caracteres_numericos():
    for i in range(10):
        caractere = str(i)
        codigo_decimal = ord(caractere)
        codigo_octal = oct(codigo_decimal)
        codigo_hexadecimal = hex(codigo_decimal)

        print (f"'{caractere}' - {codigo_decimal} - Octal: {codigo_octal} - Hexadecimal: {codigo_hexadecimal}")

def imprimir_caractere_especifico():
    caractere = input("Digite um caractere: ")
    codigo_decimal = ord(caractere)
    codigo_octal = oct(codigo_decimal)
    codigo_hexadecimal = hex(codigo_decimal)

    print (f"'{caractere}' - {codigo_decimal} - Octal: {codigo_octal} - Hexadecimal: {codigo_hexadecimal}")

def caracteres_especiais():
#Demonstração de como Python lida com caracteres especiais    
    caracteres_especiais = ['ç', 'ã']

    for caractere in caracteres_especiais:
        codigo_decimal = ord(caractere)
        codigo_octal = oct(codigo_decimal)
        codigo_hexadecimal = hex(codigo_decimal)

        print (f"'{caractere}' - {codigo_decimal} Octal: {codigo_octal} - Hexadecimal: {codigo_hexadecimal}")

#Imprime caracteres numéricos
print ("Caracteres Numéricos: ")
imprimir_caracteres_numericos()

#Imprime informações sobre um caractere específico
print ("\nCaractere específico: ")
imprimir_caractere_especifico()

#Demonstra como Python lida com caractere especiais
print ("\nCaractere Especiais: ")
caracteres_especiais()
