"""
	file:run4.py
	autor:@JoanMBQ

Deseamos obtener el costo de una carrera universitaria.
El valor promedio de cada ciclo es de 1200 dolares
el valor promedio del seguro educativo es de 100 dolares si la edad del 
estudiante es menor igual a 20 caso contrario sera de 150 dolares
Si el estudiante tiene una modalidad a distancia el numero de ciclos a 
seguir es de 10, caso contrario debera seguir 8 ciclos
Obtener la proyeccion del costo de la carrera de un estudiante
"""
#Ingreso de datos
edad = input("Ingrese su edad: ")
modalidad = input("Ingrese su modalidad:\n1.Presencial\n2.A distancia\n ")

#Declaracion de variables
edad = int(edad)
modalidad = int(modalidad)
ciclos = int
seguro = float
total_seguro = float
total = float

#Condicional para calcular los ciclos
if (modalidad == 1):
	ciclos = 8
else:
	ciclos = 10

#Condicional para calcular el valor del seguro
if (edad <= 20):
	seguro = 100
else:
	seguro = 150
total_seguro = (ciclos * seguro)
total = (ciclos * 1200) + total_seguro

#Salida de datos
print ("El total a pagar de la carrera universitaria es igual a: $%d por un total"
	" de %d ciclos y adicinal $%d de seguro por ciclo." %(total, ciclos, seguro))