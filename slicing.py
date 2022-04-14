cadena = "acitametaM ,5.8 ,otipeP ordeP"

nombre = cadena[:-13:-1]
nota = cadena[-15:-18:-1]
materia = cadena[-20::-1]

cadena_volteada = nombre + " ha sacado un " + nota + " en " + materia

print(cadena_volteada)