# Declaración de variables
alumnos = []
calificaciones = []

# Cargar el nombre y la calificación de cada alumno
for i in range(10):
    alumno = input("Ingrese el nombre del alumno: ")
    calificacion = float(input("Ingrese la calificación de %s: " % alumno))
    alumnos.append(alumno)
    calificaciones.append(calificacion)

# Ordenar las calificaciones de menor a mayor
calificaciones_ordenadas = sorted(calificaciones)

# Imprimir las calificaciones y los nombres correspondientes
print("Calificaciones de menor a mayor:")
for calificacion in calificaciones_ordenadas:
    indice = calificaciones.index(calificacion)
    alumno = alumnos[indice]
    print("%s: %.2f" % (alumno, calificacion))