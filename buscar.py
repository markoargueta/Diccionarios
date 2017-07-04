# Programa para buscar un codigo universitario digitado por el usuario
print("\tBUSCADOR DE CARNET UNIVERSITARIO ----- INGRESA TU CARNET UNIVO")

# Por ejemplo U20121234
entrada = input("Ingrese el codigo del alumno que quiere buscar: ")

# La ubicacion de la terminal debe estar en la carpeta donde este el archivo diccionario.txt
diccionario = open("diccionario.txt", "r")

contador = 0

for i in diccionario.readlines():
	# Pasar a mayuscula por si escribe "u" en lugar de "U"
	if i[:-1] == str(entrada.upper()) or i == str(entrada.upper()):
		contador+=2

if contador>1:
	print("Si estas en el diccionario")
else:
	print("No estas en el diccionario")
