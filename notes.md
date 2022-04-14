# Coder House

## Clase 1 21/03/2022

- c es un lenguaje compilado es más rápido porque se traduce todo de una a binario
- python es un lenguaje interpretado, línea por línea; es "más lento"

framework es más que librería; estructura determinada para el código y metodología del proyecto

## methods for dictionaries

```py
colores = {'amarillo':'yellow','azul':'blue','verde':'green'}
```

- colores.key(): `dict_keys(['amarillo,'azul','verde'])`
- colores.values(): `dict_keys(['amarillo,'azul','verde'])`
- colores.get(): colores.get('rojo','no hay rojo')
- colores.items(): crea una lista con clave y valor

````py
colores.items()
# dict_items([('amarillo','yellow'),('azul','blue'),('verde','green')])
for clave, valor in colores.items():
  print(clave,valor)

# amarillo yellow
# azul blue
# verde green
```

## methods for strings

- cadena.upper()
- cadena.lower()
- cadena.capitalize()
- cadena.title()
- cadena.count('amigo') # cuántas veces aparece la palabra amigo
- cadena.find('esta') # el índice en el que aparece una subcadena dentro de la misma cadena (si no encuentra, devuelve -1)
- cadena.rfid('esta') # el índice de la última ocurrencia
- cadena.split() # crea una lista con la cadena de caracteres separada por el separador indicado entre parentesis (defecto, espacios)
- ''.join() # devuelve una cadena separada a partir de una especie de separador
- cadena.strip() # devuelve una cadena borrando todos los caracteres delante y detrás de la cadena
- cadena.replace('o','0') # devolver una cadena reemplazando los subcaracteres indicados

## methids for lists

- lista.clear()
- lista.extend() # une una lista con otra





