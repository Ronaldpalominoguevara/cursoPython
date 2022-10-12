## if se le conoce como estructura de selección simple y su función es realizar o no una determinada acción o sentencia
## if else, permite que un programa ejecute unas instrucciones cuando se cumple una condición y otras instrucciones cuando no se cumple esa condición.
## elif después de su declaración if inicial.Ten en cuenta que solo se ejecutará una condición:

comida_preferida = "Tacos"
if comida_preferida == "Tacos":
	print("Te gustan los Tacos")
elif comida_preferida == "Pizza":
	print("Te gusta la Pizza")
elif comida_preferida == "Hamburguesa":
	print("Te gustan las hamburguesas")
else:
	print("Te gusta otra comida")