import time
#Ariel Fernández Gualdrón
class figuras_geometricas1:
	base=0
	altura=0
	area_triangulo=0
	area_rectangulo=0
	print("Bienvenido el dia de hoy calcularemos el area del triangulo y del rectangulo")
	time.sleep(2)
	print("ingrese los datos en el orden que se solicita")
	time.sleep(2)
	base= int(input("por favor ingrese la base = "))
	time.sleep(2)
	altura= int(input("ahora por favor ingrese la altura = "))
	area_triangulo= ((base* altura)/2)
	area_rectangulo=(base*altura)
	time.sleep(2)
	print("El area del triangulo es ",area_triangulo)
	time.sleep(1)
	print("El area del rectangulo es ",area_rectangulo)
    time.sleep(1)
    print("Gracias")
