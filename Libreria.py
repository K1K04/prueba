import json 
with open("book.json") as fichero:
    datos=json.load(fichero)
    
"""¿Cuántos libros hay en la librería?
Recibe un límite inferior y superior para el precio y muestra todos los libros cuyo precio esta en ese intervalo.
Recibe una cadena por teclado, y muestra el título y el año de publicación de los libros cuyo título empiece por la cadena introducida.
Devuelve todos los títulos de los libros con la lista de sus autores."""
    
def cuenta_libros(datos):
   return len(datos['bookstore']['book'])
    
def seleccionar_por_precios(datos,pmax,pmin):
	libros=[]
	for libro in datos["bookstore"]["book"]:
		precio=float(libro["price"])
		if precio<=pmax and precio>=pmin:
			libros.append(libro["title"]["__text"])
	return libros

def seleccionar_por_titulo(doc,titulo):
	libros=[]
	for libro in doc["bookstore"]["book"]:
		if libro["title"]["__text"].startswith(titulo):
			libros.append((libro["title"]["__text"],libro["year"]))
	return libros	

def seleccionar_autores(doc):
	libros=[]
	for libro in doc["bookstore"]["book"]:
		autores=[]
		if isinstance(libro["author"],list):
			for autor in libro["author"]:
				autores.append(autor)
		else:
			autores.append(libro["author"])
		libros.append((libro["title"]["__text"],autores))
	return libros
    
print('Bienvenido a la libreria de kiko')

num_libros = len(datos['bookstore']['book'])

print(f'Hay {num_libros} libros en la libreria')

precio_max=float(input("Precio maximo:"))
precio_min=float(input("Precio minimo:"))
for libro in seleccionar_por_precios(datos,precio_max,precio_min):
	print(libro)
 
cadena=input("Dime el nombre del libro y te dire el año de publicacion:")
for titulo,autor in seleccionar_por_titulo(datos,cadena):
	print(autor,titulo)
 
for titulo,autores in seleccionar_autores(datos):
	print(titulo)
	for autor in autores:
		print(autor)	
	print("")