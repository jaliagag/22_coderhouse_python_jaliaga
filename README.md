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

## clase 9

- parámetro: durante la definición de la función
- argumento: durante la llamada de la función

```py
de nombre(parametro): # parámetro
  sentencias
  return <>

nombre(a) # a es el argumento que se le pasa a la función
```

## clase 11 - excepciones



## clase 12-13-14

### clases

- `clase` elemento principal
- `atributos` características
- `métodos` funcionalidades

Tipos de relaciones:

- agregación / composición: entre clase TODO y una clase PARTE que es componente de todo. la clase TODO es un objecto _contenedor_, que contiene otros objetos. Por ejemplo, una clase _auto_ (objeto contenedor) contiene adentro una clase _motor_ con sus características (#--)
- asociación: relación semántica _entre objetos no relacionados_. una clase usa a otra clase para realizar algo. clase _persona_ tiene una clase _auto_ (<--)
- generalización / especialización

Cardinalidad. indicar el número de objetos que están en relación. las personas pueden tener muchos autos (`*..*`), pero un auto solo puede tener un motor y el motor solo puede pertener a un auto (`1 1`).

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

#### herencia

proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. la clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

```py
class Animal:
  pass

# creamos una clase hija que hereda de la clase padre
class Perro(Animal):
  pass

```

Filosofía DRY: don't repeat yourself

#### super

la función super nos permite acceder a los argumentos de la clase padre desde una de sus hijas

```py
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
```

Para agregar un parámetro nuevo a nuestra clase perro, tenemos dos alternativas, una verbosa, la de toda la vida donde declaramos los atributos de la clase padre o podemos usar `super` (para DRY) de esta manera:

```py
class Perro(Animal):
  def __init__(self,especie,edad,dueno):
    # alternativa caca, verbosa
    #self.especie = especie
    #self.edad = edad
    #self.dueño = dueno
    super().__init__(especie,edad)
    self.dueno = dueno
```

con `super().__init__(especie,edad)` llamamos a esos atributos y no tenemos que volver a declararlos - después simplemente le agregamos el nuevo atributo

#### herencia múltiple

una clase hereda de varias clases padre en vez de una sola. dos maneras de hacerlo:

```py
# 1
class Clase1:
  pass
class Clase2:
  pass
class Clase3(Clase1,Clase2):
  pass

# 2
class Clase1:
  pass
class Clase2(Clase1):
  pass
class Clase3(Clase2):
  pass
```

qué pasa si llamo a un método que todas las clases tienen en común? cuál se llama? la función MRO (Method Resolution Order) - esta función nos devuelve una tupla con el orden de búsqueda de los métodos: se empieza en la propia clase y se va subiendo hasta la clase padre, de izquierda a derecha.

```py
print(Clase3.__mro__)
# (<class '__main__.Clase3'>, <class '__main__.Clase2'>, <class '__main__.Clase1'>, <class 'object'>)
```

al final de la tupla vemos la clase object. en realidad todas las clases en python heredan de una clase genérica object, aunque no lo especifiquemos explícitamente.

El orden de herencia depende del orden en el que las clases están pasadas (no es lo mismo `Clase4(Clase1,Clase2,Clase3)` que `Clase4(Clase2,Clase3,Clase1)`)

#### polimorfismo

los objetos pueden tomar distintas formas, es decir, los objetos de clases diferentes pueden ser accedidos usando la misma interfaz y mostrar un comportamiento distinto (_distintas formas_) según cómo sean accedidos. una operación puede presentar distintos comportamientos en distintas instancias. el comportamiento depende de los tipos de datos utilizados en la operación - este concepto está muy relacionado con la herencia.

```py
class Persona():
  def __init__(self):
    self.cedula = 12345678
  def mensaje(self):
    print('mensaje desde la clase persona')

class Obrero(Persona):
  def __init__(self):
    self.__especialista = 1
  def mensaje(self): # esta es una instancia de polimorfismo
    print('mensaje desde la clase obrero')
```

Podemos sustituir un método proveniente de la clase padre en la clase hija. tiene que ser un método con el mismo nombre y parámetros pero debe tener otra conducta.

#### duck typing

si un objeto tiene los métodos que nos interesan, nos basta, siendo su tipo irrelevante. a python le da igual los tipos de los objetos, lo único que importa son los métodos

```py
class Pato:
  def hablar(self):
    print('cuac')

p = Pato()
p.hablar()
# cuac
```

no es necesario especificar los tipos, simplemente decimos que el parámetro de entrada tiene el nombre `p` 

```py
def llama_hablar(x):
  x.hablar()

llamar_hablar(p)
# cuac
```

cuando llamemos a la función, le da igual el tipo al que pertenece `p` siempre y cuando tenga la función `hablar()`

_lo importante son los métodos, no los tipos de las clases_ - podemos ver también duck typing en la función _len()_ y en el uso del operador `*`

## clase 15

### módulos y paquetes









