import filecmp

i = 0
while(i == 0):
	extension = input("Escriba la extensión del archivo: ")
	file1 = input("Ecriba el nombre del archivo 1 sin la extensión: ")
	file2 = input("Ecriba el nombre del archivo 2 sin la extensión: ")

	try:
		result = filecmp.cmp(file1 + '.' + extension, file2 + '.' + extension)
	except FileNotFoundError as fnf:
		print(fnf)
	else:
		if result:
			print("Los archivos son iguales")
		else:
			print("Los archivos son diferentes")
	
		i = input("Ingrese 0 para continuar: ")
		i = int(i) if i == "0" else i
