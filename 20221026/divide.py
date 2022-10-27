"""
Programa: Divide
Requisito: Faça um programa que leia dois números inteiros, calcule o quociente deles e mostre o resultado na tela.
Autor: Fernando Mees
Data: 26/10/2022
Versao: 0.0.1
"""

# Entrada
x = int(input("Insira o primeiro numero inteiro: "))
y = int(input("Insira o segundo numero inteiro: "))
while y == 0:
    y = int(input("Insira o segundo numero inteiro diferente de zero: "))

# Processamento
z = x / y

# Saida
print(f"O quociente dos numeros {x} e {y} e igual a {z}.")
