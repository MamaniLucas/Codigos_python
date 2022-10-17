 #listar 

#tener un boton para seleccionar todo
print("Listado de compras")
cola = ["Camote", "lechuga"]  
print(cola)

 #agregar a la cola 
print(" Agregando a Listado de compras")

cola.append("PAN")
print("Se necesita:", cola[-1])
cola.append("Mantequilla")
print("Se necesita:", cola[-1])
cola.append("Cebolla")
print("Se necesita:", cola[-1])
cola.append("Tomate")
print("Se necesita:", cola[-1])
cola.append("Brocolí")
print("Se necesita:", cola[-1])

print(cola)
#eliminar

print("SALIDA")

atendido = cola.pop(0)
print("Se compro:", atendido)
atendido = cola.pop(0)
print("Se compro:", atendido)
atendido = cola.pop(0)
print("Se compro:", atendido)
atendido = cola.pop(0)
print("Se compro:", atendido)


#esta vacia al no tener elemetnos 
# ver el tamaño
print(cola)

