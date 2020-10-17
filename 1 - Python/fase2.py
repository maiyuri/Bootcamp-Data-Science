# -*- coding: utf-8 -*-
"""Fase2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_N5YNfVTUy73ZdTJV1Tvgupp51xUUErR

Crie um algoritmo em Python que peça 2 números e imprima o maior deles.
"""

# INSIRA SEU CÓDIGO AQUI
print("Me dê dois números e eu direi qual deles é o menor")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

if num1 < num2: 
  print(f"O número {num1} é menor que {num2} que foi o primeiro número a ser adicionado")
else:
  print(f"O número {num2} é menor que {num1} que foi o segundo número a ser adicionado")

"""Crie um algoritmo em Python que peça um valor e mostre na tela se o valor é positivo ou negativo."""

# INSIRA SEU CÓDIGO AQUI
print("Me dê um número e direi se ele é positivo ou negativo.")
num = int(input("Número: "))
if num > 0:
  print(f"O número {num} é positivo.")
else: 
  print(f"O número {num} é negativo.")

"""Crie um algoritmo em Python que verifique se uma letra digitada é vogal ou consoante."""

# INSIRA SEU CÓDIGO AQUI
print("Digite uma letra e eu direi se é vogal ou consoante.")
letra = input("Letra: ").upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
  print(f"{letra} é vogal")
elif letra.isnumeric():
  print(f"{letra} é número")
else: 
  print(f"{letra} é consoante.")

"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
* "Aprovado", se a média alcançada for maior ou igual a sete;
* "Reprovado", se a média for menor do que sete;
* "Aprovado com Distinção", se a média for igual a 10.
"""

# INSIRA SEU CÓDIGO AQUI
nota1 = float(input("Insira duas notas e eu direi qual foi a sua média. \nNota1: "))
nota2 = float(input("Nota2: " ))

media = (nota1+nota2)/2

if media == 10:
  print(f"Sua média foi de {media}! Parabéns! Aprovada(o) com a nota máxima!!!")
elif media >= 7:
  print(f"Sua média foi de {media}, parabéns! Você foi aprovada(o)!")
else: 
  print(f"Sua média foi de {media}, infelizmente você foi reprovado.")

"""Crie um algoritmo em Python que leia três números e mostre o maior deles."""

# INSIRA SEU CÓDIGO AQUI
num1 = float(input("Insira três número e eu direi qual é o número maior.\nNúmero1: "))
num2 = float(input("Número2: "))
num3 = float(input("Número3: "))

lista = [num1, num2, num3]
lista.sort()
print(lista[2])

"""Crie um algoritmo em Python que leia três números e mostre o maior e o menor deles."""

# INSIRA SEU CÓDIGO AQUI
num1 = float(input("Insira três número e eu direi qual é o número maior.\nNúmero1: "))
num2 = float(input("Número2: "))
num3 = float(input("Número3: "))

lista = []
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.sort()
print(f"{lista[0]} é o número menor e {lista[2]} é o número maior.")

"""Faça um programa que pergunte o preço de 5 produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

# INSIRA SEU CÓDIGO AQUI
val_prod = [] 

for c in range(0, 5):
  val_prod.append(float(input(f"Valor({c+1}): ")))

val_prod.sort()
print(f"O produto mais barato é do valor de {val_prod[0]}")

"""Crie um algoritmo em Python que leia três números e mostre-os em ordem decrescente."""

# INSIRA SEU CÓDIGO AQUI
num = []

for r in range(0,3):
  num.append(float(input(f"Número {r+1}: ")))

num.sort(reverse=True)
print(f"A ordem decrescente dos números adicionados é: {num}")

"""As Organizações Mendéz resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes em Python. Faça um programa que receba o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

* salários entre 680,00 e 800,00 : aumento de 15%<br>
* salários entre 800,00 e 2500,00 : aumento de 10%<br>
* salários de 2500,00 em diante : aumento de 5% após o aumento ser realizado.

Informe na tela:
* o salário antes do reajuste;
* o percentual de aumento aplicado;
* o valor do aumento;
* o novo salário, após o aumento.
"""

# INSIRA SEU CÓDIGO AQUI
salario = float(input("Insira o valor do seu salário atualmente: R$ "))

if salario >= 680.00 and salario < 800.00:
  percentual = 0.15
elif salario >= 800.00 and salario < 2500.00:
  percentual = 0.10
elif salario > 2500.00:
  percentual = 0.5

aumento = salario * percentual
novo_salario = salario + aumento

print(f"- Salário antes do reajuste: R${round(salario, 2)} \n- Percentual aplicado: {round(percentual*100)}%\n- Valor do aumento: R${round(aumento, 2)}\n- Novo salário: R${round(novo_salario, 2)} ")