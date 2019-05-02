"""
	file:run2.py
	autor:@JoanMBQ
"""

from MisVariables import *

# Uso de condicional simple

nota = input("Ingrese nota 1: ")
nota2 = input("Ingrese nota 2: ")

nota = int(nota)
nota2 = int(nota2)

if nota >= 18:
	print ("%s, Su valor de nota es: %d" % (mensaje, nota))
else:
	print ("%s, Su valor de nota es: %d" % (mensaje2, nota))

if nota2 >= 17:
	print ("%s, Su valor de nota es: %d" % (mensaje, nota2))
else:
	print ("%s, Su valor de nota es: %d" % (mensaje2, nota2))