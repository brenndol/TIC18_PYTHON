import random

nomeCompleto = "Brenndol Pinto Magalhães"
nome, sobrenome = nomeCompleto.rsplit(maxsplit=1)
if nome < sobrenome:
    print(f"{nome} antecede {sobrenome} na ordem alfabetica. ")

elif nome > sobrenome:
    print(f"{sobrenome} antecede {nome} na ordem alfabetica. ")
    
else:
    print("Os nomes sao iguais na ordem alfabetica. ")

print(f"Quantidade de caractere no nome: {len(nome)}")
print(f"Quantidade de caractere no sobrenome: {len(sobrenome)}")

if nome == nome[::-1]:
    print(f"{nome} é um palíndromo.")
else:
    print(f"{nome} não é um palíndromo.")
