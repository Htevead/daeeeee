# lista=[5, 7, 2, 9, 10, 2]
# #      0  1  2  3   4  5

# lista=[5, 7, 2, 9, 10, 2]
# #      -6 -5 -4 -3 -2 -1

# print(lista[])
# # print(lista[])

# Promedio de notas con un listado
# notas=[55, 67, 34, 47, 70]
# c=0
# suma=0
# for nota in notas:
#     suma+=nota
#     c+=1
# prom=suma/c
# print("El promedio es", round(prom))


# Nombres y nueva funcion len() con for
# len() lee todos los caracteres que tenga una variable y los cuenta, ejemplo con la funcion nombres, si ponemos len(nombres) 
# y con un print lo mostramos, daria como resultado el numero que tenga la lista, en este caso es un 3
# nombres=["Robin", "Noelia", "Coni"]
# apellidos=["Hood", "Maldonado", "Chan"]

# print(len(nombres))

# for i in range(len(nombres)):
#     print(f"Su nombre es {nombres[i]} {apellidos[i]}")


# En este caso len cuenta los caracteres de cualquier objeto, si es una lista cuenta el numero de objetos, si es un string cuenta los caracteres, como sabemos que for inicia en 0
# y el indice de la lista tambien inicia en 0 por lo tanto si queremos que cuenta la lista pondriamos len(frutas) 
# si queremos que cuente los caracteres ponemos la variable que pusimos en el for, en este caso es 'fruta'
# frutas=["Sandia", "Melon", "Chirimoya"]

# for fruta in frutas:
#     print(f"La {fruta} tiene {len(fruta)} caracteres")


# ahora veremos con marcas de auto, que marcas de auto tienen una a

# autos=["Audi", "Toyota", "BMW", "KIA", "Mercedez"]

# for auto in autos:
#     print(auto)
#     if "a" in auto.lower():
#         print("La marca tiene una a")
#     else:
#         print("No tiene a")

