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

```py
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

## methods for lists

- lista.clear()
- lista.extend() # une una lista con otra
- lista.insert(posición,ítem) # agregar un ítem en un índice específico
- lista.reverse() # dar vuelta a una lista (para los strings, podemos convertir a lista y después hacemos join)
- lista.sort() # de menor a mayor; si ponemos .sort(reverse=True) de mayor a menor

## clase 8

- binarios: archivos que mejoran su eficienta pero los datos están guardados bajo agrupaciones de bytes; machine code
- texto

### Leer archivos

- permisos de escritura: `-r`
- `read` leer el archivo entero
- `readline` leer solo la primera línea
- `readlines` leer cada línea
- `seek` - acceder a una ubicación en particular, es decir, empezar la lectura desde la posición indicada

## clase 12-13-14

### clases

#### crear una clase

```py
class Perro:
  # atributos de clase
  # atributo común a todas las clases que se creen
  especie = "mamifero"
  # constructor de la clase
  def __init__(self,nombre,raza):
    # atributos de la instancia
    self.nombre = nombre
    self.raza = raza

  # métodos
  def ladra(self):
    print('wiwi!')

  def camina(self, pasos)
    print(f'camino {pasos} pasos')

  # métodos especiales
  # imprimir el contenido del objeto
  # si hacemos print(clase) nos devuelve esto
  def __str__(self):
    return 'the values are {self.nombre} {self.raza}'
class Vector:
  def __init__(self,data):
    self.data = data

  # ver length del objeto - si hacemos len(clase) nos devuelve este valor
  def __len__(self):
    return len(self.data)

  # leer los elementos mediante el uso de corchetes
  # v[1]
  # esto solo nos retorana info
  def __getitem__(self,pos):
    return self.data[pos]

  # para modificar tenemos que crear __setitem__
  def __setitem__(self,pos,value):
    self.data[pos] = value

  # clase iterable
  def __iter__(self):
    for pos in range(0,len(self.data)):
      yield f'Value[{pos}]: {self.data[pos]}'

# crear un perro
perro1 = Perro('obama','labrador negro')
print(f'nombre: {perro1.nombre}')
print(f'raza: {perro1.raza}')
print(f'especie: {perro1.especie}')
perro1.ladra()
perro1.camina(5)

# crear vector
v = Vector([1,2])
v[1] = 20
# v = [1,20]
for vec in v:
  print(vec)
```

#### relación entre clases

supongamos que tenemos una clase `Perro` y una clase `Persona` - podríamos crear un objeto `persona1` que incluya un perro.

```py
class Perro:
  ...
class Persona:
  ...
perro1 = Perro('obama','labrador negro')
persona1 = Persona('José','Aliaga',perro1)
```

#### encapsulamiento

ocultamiento de los estados internos de una clase al exterior - hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desd afuera

- `__` privado --> imposible acceder desde el exterior de la clase

```py
class Persona:
  def __init__(self,id):
    self.__id = id # << ocultamos id

  def __process(self): # ocultamos el método
    print('hola')
```

#### encapsulamiento



## clase 15

### módulos y paquetes









