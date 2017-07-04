# Programa para hacer un diccionario con los codigos universitarios.
print("CREADOR DE CARNET DE LA UNIVO")

carnet = open("carnet.txt", "r+")

for i in range(2000, 2020):
	for j in range (0, 10000):
		if j<10:
			carnet.writelines("U"+str(i)+"000"+str(j)+"\n")
		elif j<100:
			carnet.writelines("U"+str(i)+"00"+str(j)+"\n")
		elif j < 1000:
			carnet.writelines("U"+str(i)+"0"+str(j)+"\n")
		else:
			carnet.writelines("U"+str(i)+str(j)+"\n")

print("Diccionario creado")