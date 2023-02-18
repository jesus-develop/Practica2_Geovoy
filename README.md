# Practica2_Geovoy

En este código se utiliza una lista llamada "alumnos" para almacenar los nombres de los estudiantes, y otra lista llamada "calificaciones" para almacenar las calificaciones de cada uno.

Primero se solicita al usuario que ingrese el nombre y la calificación de cada uno de los 10 alumnos, y se almacenan en las listas correspondientes utilizando un bucle for.

Luego se utiliza la función sorted() para ordenar las calificaciones de menor a mayor, y se almacenan en una nueva lista llamada "calificaciones_ordenadas".

Finalmente se recorre la lista de calificaciones ordenadas, y para cada calificación se busca el índice correspondiente en la lista de calificaciones original utilizando el método index(). Con ese índice se obtiene el nombre del alumno correspondiente de la lista de nombres, y se imprime en pantalla en orden de menor a mayor, junto con su calificación.
