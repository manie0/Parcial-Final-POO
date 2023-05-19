# Parcial-Final-POO
Presentación parcial Final Programación orientada a Objetos
# ¿Como usar?
Crear objetos necesarios:

-) Crear una instancia de la clase Residuos con valores de vidrio, papel, plástico, metal y orgánicos.

Ejemplo:

`residuos = Residuos(2.5, 1.8, 3.2, 0.9, 4.7)`

-) Crear una instancia de la clase Camion con un conductor, los residuos creados anteriormente y los asistentes correspondientes.

Ejemplo:

`camion = Camion("Juan", residuos, "Maria", "Pedro")`

-) Crear instancias de la clase Turno con valores de inicio, fin, el camión (Se pueden instanciar varios camiones si asi se desea, por comodidad se usa el mismo) creado anteriormente y un día específico.

Ejemplo:

```
turno1 = Turno("08:00:00", "16:00:00", camion, 1)
turno2 = Turno("08:00:00", "16:00:00", camion, 1)
```

-) Crear una instancia única de TrashCity utilizando el patrón Singleton.

Ejemplo:

`trash_city = TrashCity()`

-) Agregar un observer a TrashCity para recibir notificaciones de actualizaciones de rutas.

Ejemplo:

```
observer = Observer()
trash_city.agregar_observer(observer)
```

-) Crear instancias de la clase Ruta con una lista de puntos y un id de ruta. Agregar los turnos creados anteriormente a las rutas correspondientes.

Ejemplo:

```
ruta1 = Ruta([(40.7128, -74.0060), (40.7306, -73.9352), (40.7488, -73.9857)], 1)
ruta2 = Ruta([(40.7128, -74.0060), (40.7306, -73.9352)], 2)
ruta1.turnos.append(turno1)
ruta2.turnos.append(turno2)
```

-) Agregar las rutas a TrashCity utilizando el método agregar_ruta.

Ejemplo:

```
trash_city.agregar_ruta(ruta1)
trash_city.agregar_ruta(ruta2)
```

-) Iterar sobre las rutas utilizando el RutaIterator y verificar que se recorren todas las rutas.

Ejemplo:

```
iterator = RutaIterator(trash_city.rutas)
for ruta in iterator:
    print(f"Recorriendo la ruta {ruta.id_ruta}")
```


-) Obtener la cantidad de vidrio para un día específico utilizando el método cantidad_vidrio_por_dia del RutaIterator y verificar que se obtenga el valor correcto.

Ejemplo:

```
cantidad_vidrio = iterator.cantidad_vidrio_por_dia(1)
print(f"Cantidad de vidrio para el día 1: {cantidad_vidrio}")
```

# Codigo para probar
En el Archivo "FinalPOO" al final hay un espacio para pegar un codigo de prueba, puede poner este y correr el archivo:

```
# ¿Como usar?
# Crear objetos necesarios
residuos = Residuos(2.5, 1.8, 3.2, 0.9, 4.7)
camion = Camion("Juan", residuos, "Maria", "Pedro")
turno1 = Turno("08:00:00", "16:00:00", camion, 1)
turno2 = Turno("08:00:00", "16:00:00", camion, 1)

# Crear instancia única de TrashCity
trash_city = TrashCity()

# Agregamos observer
observer = Observer()
trash_city.agregar_observer(observer)

ruta1 = Ruta([(40.7128, -74.0060), (40.7306, -73.9352), (40.7488, -73.9857)], 1)
ruta2 = Ruta([(40.7128, -74.0060), (40.7306, -73.9352)], 2)
ruta1.turnos.append(turno1)
ruta2.turnos.append(turno2)

trash_city.agregar_ruta(ruta1)
trash_city.agregar_ruta(ruta2)

# Iterar sobre las rutas
iterator = RutaIterator(trash_city.rutas)
for ruta in iterator:
    print(f"Recorriendo la ruta {ruta.id_ruta}")

# Obtener la cantidad de vidrio para el día 1
cantidad_vidrio = iterator.cantidad_vidrio_por_dia(1)
print(f"Cantidad de vidrio para el día 1: {cantidad_vidrio}")
```
# Por ultimo (Tests)
Hay 2 Archivos de test, uno para la actualización de los observers y otro para la funcion de calculo de vidrio del iterator 

