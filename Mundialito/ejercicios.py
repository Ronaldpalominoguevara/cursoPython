###definir una funcion max()que tome como argumento un array de numeros que devuelva el mayor del array
# def comp(numenor,numayor):
#  	if numenor < numayor:
#  		print(" es mayor que ".format(numayor, numenor))
# elif numenor > numayor:
# print("es mayor que ".format(numenor, numayor))
#  else: 
#  	print("son el mismo numero")

# if __name__ == '__main__':
#  	num1 = float(input("ingresa un numero: "))
# num2 = float(input("ingresa otro numero: "))
# comp(num1, num2)


##Escribir una funcion que alamcene en una lista los siguientes precios, 50,75,46,22,80,65,8, y muestre por pantalla le menor y el mayor de los precios.


# prices = [50, 75, 46, 22, 80, 65, 8]
# min = max = prices[0]
# for price in prices:
#     if price < min:
#         min = price
#     elif price > max:
#         max = price 
# print("El mínimo es " + str(min)) 
# print("El máximo es " + str(max))



##Escribir una funcion mas larga() que tome una array de palabras y devuelva la mas larga 
# def mas_larga(lista):
#  	palabra_mayor = len(lista[0])
#     palabra_mostrar = lista[0]

# for palabra in lista:
#  	if palabra_mayor <= len(palabra):
#  		palabra_mostrar = palabra
#         palabra_mayor = len(palabra)
# else:
#  			palabra_mostrar = palabra_mostrar

# print(palabra_mostrar)


# lista = ["a", "afgdfgfdb", "dsfdsfdsfsdfsdfsd"]
# mas_larga(lista)


 ## Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que       
# def creador_dict(cadena):
#   '''Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
#   lista1= cadena.split()
#   dict1={}
#   for i in lista1:
#     if i in dict1:
#       dict1[i] +=1
#     else:
#       dict1[i]= 1
#   return dict1

# def contador_dict(dictionario):
#   '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
#   palabra_frecuente= ''
#   cantidad=0
#   for keys,values in dictionario.items():
#     if values > cantidad:
#       cantidad= values
#       palabra_frecuente= keys
#   return palabra_frecuente,cantidad
# entrada=input('Ingrese su cadena de caracteres: ')
# print(creador_dict(entrada))
# print(contador_dict(creador_dict(entrada)))