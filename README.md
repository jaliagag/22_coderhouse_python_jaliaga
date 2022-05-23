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

## clase 15 - módulos y paquetes

para pasarle argumentos a nuestro programa tenemos que agregar el módulo `sys`

```py
import sys
print(sys.argv) # para ver los argumentos
```

un módulo es un archivo que consta de código python. en realidad es un objeto de python con atributos de nombres arbitrarios que puede enalzar y luego referenciar.

para llamar a un módulo desde otro archivo, si está en el mismo directorio:

```py
#import <nombre del archivo>
import funciones_matematicas

funciones_matematicas.sumar(4,11)

# importar función específica
from funciones_matematicas import suma
# importar todas *
```

#### paquetes

carpetas para organizar módulos por categorías. creamos una carpeta y dentro de ella tener un archivo llamado `__init__.py`

```console
clase15
├── menu.py 
├── mi_primer_paquete
│   ├── __init__.py
│   ├── modulo1.py
│   ├── modulo2.py
│   └── __pycache__
│       ├── __init__.cpython-39.pyc
│       ├── modulo1.cpython-39.pyc
│       └── modulo2.cpython-39.pyc
```

Desde menú, llamamos al paquete:

```py
from mi_primer_paquete.modulo1 import Persona
from mi_primer_paquete.modulo2 import llamado_modulo2


persona1 = Persona('octavio','aliaga')
print(persona1)

llamado_modulo2()
```

##### paquetes redistribuibles

```py
from setuptools import setup

setup(
    name='jalaiaga_primer_paquete',
    version='1.0',
    description='clase 15',
    author='jaliaga',
    authoer_email='jmfaliaga@gmail.com',

    packages=['mi_primer_paquete']

)
```

```console
$ 
.
├── mi_primer_paquete
│   ├── __init__.py
│   ├── modulo1.py
│   ├── modulo2.py
│   └── __pycache__
│       ├── __init__.cpython-39.pyc
│       ├── modulo1.cpython-39.pyc
│       └── modulo2.cpython-39.pyc
└── setup.py
$ python setup.py sdit

$
.
├── dist
│   └── jalaiaga_primer_paquete-1.0.tar.gz
├── jalaiaga_primer_paquete.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── mi_primer_paquete
│   ├── __init__.py
│   ├── modulo1.py
│   ├── modulo2.py
│   └── __pycache__
│       ├── __init__.cpython-39.pyc
│       ├── modulo1.cpython-39.pyc
│       └── modulo2.cpython-39.pyc
└── setup.py
```

Usar el paquete que nos pasó alguien: nos paramos en el mismo directorio que el archivo que nos pasaron y ejecutamos: `pip3 install <nombre_paquete.tar.gz>`

#### paquetes externos

##### Collections

el módulo collections nos ayuda a completar y manipular las estructuras de datos de forma eficiente - `from collections import *` - _namedtuple_ (`from collections import namedtuple`) permite añadir nombres explícitos a cada elemento de una tupla para hacer que estos significados sean claros en el programa:

```py
from collections import namedtuple

Fish = namedtuple('Fish',['name','species','tank']) # << crea una clase

miPrimerPez = Fish('sam','tiburón','tanque grande')
print(miPrimerPez)
# Fish(name='sam', species='tiburón',tank='tanque grande')
# transformar tupla en diccionario
print(miPrimerPez._asdict())
# {'name':'sam', 'species':'tiburón','tank':'tanque grande'}
```

##### Counter

subclase de diccionar utilizada para realizar cuentas con diccionarios y listas

```py
from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]

print(Counter(l))

#Counter({1: 4, 2: 3, 3: 2, 4: 1})

estudiantes = 'jose paula simba laura brenda nadia jose'
print(Counter(estudiantes))
print(Counter(estudiantes.split()))

#Counter({'a': 8, ' ': 6, 's': 3, 'e': 3, 'j': 2, 'o': 2, 'u': 2, 'l': 2, 'i': 2, 'b': 2, 'r': 2, 'n': 2, 'd': 2, 'p': 1, 'm': 1})
#Counter({'jose': 2, 'paula': 1, 'simba': 1, 'laura': 1, 'brenda': 1, 'nadia': 1})
```

<https://docs.hektorprofe.net/python/modulos-y-paquetes/modulo-collections/>

##### Datetime

```py
from datetime import datetime

dt = datetime.now()

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
```

crear una fecha usando el constructor de esta clase

```py
dt = datetime(2000,1,1)
print(dt)
# 2000-01-01 00:00:00
```

cambiar uno de los parámetros: replace

```py
dt = dt.replace(year=3999)
print(dt)

datetime.datetime(3000,1,1,0,0)
```

Formateando la forma en que presentamos la imagen:

```py
dt.strftime("%A %d %B %Y %I:%M")
Monday 23 May 2022 09:06
```

- %A - día
- %d - número de día
- %B - mes
- %Y - año
- %I - hora
- %M - minuto

con la función `timedelta()` se pueden sumar o restar fechas:

```py
from datetime import datetime,timedelta

dt = datetime.now()
# generamos 14 días con 4 horas y 1000 segundos de tiempo
t = timedelta(days=14,hours=4,seconds=1000)
# lo operamos con el datetime de la fecha y hora actual
dentro_de_dos_semanas = dt + t
```


##### Math
##### Random


## clase 17 django 1 - 18/05/2022

patrón `mvc` - arquitectura que nos permite tener una organización adecuada de nuestro código

- modell: maneja los datos y el acceso a ellos
- view: lo que el usuario ve
- controller: interacción los datos y lo que el usuario, lógica de negocio; 

el usuario usa el _controlador_ que actualiza el _modelo_ y actualiza la _vista_ que es lo que ve el usuario

nosotros no vamos a manejar más en la interacción del controlador y el modelo

django modifica el MVC por el MTV; modelo, template, view

django: según la URL tendremos una vista; el template tiene la estructura del controlador; la vista interactua directamente con el template y con el modelo. página12

- `django-admin startproject <nombreProyecto>`
- `python manage.py migrate`
- `python manage.py runserver`

















