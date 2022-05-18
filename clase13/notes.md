# oop 

[link](https://colab.research.google.com/drive/1QF620fUDd6__5qfbFFFAE2-NtsGzwfFp#scrollTo=g3_aOL8_oU1P)

Clase vacía:

```py
class Perro:
  pass
```

Creamos 2 objetos del tipo Perro, instanciamos 2 veces a la clase perro para crear 2 variables que son objetos

```py
perro1 = Perro()
perro2 = Perro()
# dos perros que tienen las mismas características pero son distintos
```

- método constructor: `__init__` permite generar automáticametne la creación de nuestro objeto; inicializar (dar valores) a los miembros de datos de la clase cuando se crea un objeto de la clase - es llamado automáticamente cuando se cree un objeto
- self: convención de python que representa la instancia de nuestra clase - siempre va al inicio; parámetro del método para acceder a los métodos y atributos de las instancias; **variable que representa la instancia de la clase**;
- atributo de instancia, del objeto que hemos creado
- atributo de clase
- el uso de `__` significa que el método está reservado para un uso especial del lenguaje - solamente para trabajar con atributos de instancia

```py
class Perro:
  # atributo de clase - todos objetos van a tener estos atributos en común, no lo podemos modificar
  especie = "Mamífero"
  # el constructor
  def __init__(self,nombre,raza):
    # atributos de instancia
    self.nombre = nombre
    self.raza = raza

obama = Perro('Obama','Labrador')
print(obama) # nos muestra el espacio del objeto en memoria
print(f'mejor verlo atributo por atributo {obama.nombre}, {obama.nombre}')
```

## métodos 

```py
class Perro:
  # atributo de clase - todos objetos van a tener estos atributos en común, no lo podemos modificar
  especie = "Mamífero"
  # el constructor
  def __init__(self,nombre,raza):
    # atributos de instancia
    self.nombre = nombre
    self.raza = raza

  # método sin argumentos
  def ladrar(self):
    print(f'{self.nombre} dice guau!')
  # método con argumentos
  def caminar(self, pasos):
    print(f'di {pasos} pasos')

obama = Perro('Obama','Labrador')
obama.caminar(8)
obama.ladrar()
```

si NO tiene argumentos, le clavamos self para hacer al mismo objeto que estamos creando;

## métodos especiales

tienen doble guión bajo

```py
class Perro:
  def __init__(self, nombre, raza, especie):
    self.nombre = nombre
    self.raza = raza
    self.especie = especie
  def __str__(self):
    return "\nNombre", self.nombre+", Raza:"+ self.raza+", Especie:"+self.especie

obama = Perro('obama','labrador','negro')
# antes cuando hacíamos un print a obama nos daba el espacio en memoria
# como agregamos el método especial __str__, ahora al hacer un print nos devuelve la info formateada como la declaramos
print(obama) 
```

- `__len__` : obtener cantidad de elementos del objeto
- `__getitem__` : obtener un objeto para el usuario lo pueda leer, la posición - es neceario el uso de `[]`
- `__setitem__` : acceder al objeto y cambiarlo
- `__del__` : borrar los datos y liberar memoria

```py
class Vector:
  def __init__(self,data):
    self.data = data
#  def __init__(self, specialties):
#    self.especialidades = specialties
  def __len__(self):
    return len(self._data)
  def __getitem__(self,pos):
    return self._data[pos]
  def __setitem__(self,pos,value):
    self._data[pos] = value

v = Vector([1,2])
v[1]=20 # acá estamos usando el setitem
```

- `_data` : 
- `__data` : 

#### método anidamiento uno

_RECOMENDADA_

```py
class Persona:

    def __init__(self, nombre, apellido, perro):
        self.nombre = nombre
        self.apellido = apellido
        self.perro = perro


    def __str__(self):
        return "Mi nombre es: " +self.nombre +" " +self.apellido +"\n" +self.perro.__str__()


persona1 = Persona("Nico", "Perez", perro1)
```

#### método anidamiento dos

```py
class Sueldo:

    def __init__(self, sueldo):
        self.sueldo = sueldo

    def __str__(self):
        return f"\nSUELDO: {self.sueldo}"


    class Empleado:

        def __init__(self, nombre, puesto):
            self.nombre = nombre
            self.puesto = puesto
            self.sueldo = Sueldo(1200)


        def __str__(self):
            return f"NOMBRE: {self.nombre}\nPUESTO: {self.puesto}\n" +self.sueldo.__str__()

s1 = Sueldo(200)
emp1 =  Sueldo.Empleado("Nico", "Profe")

print(f"RESULTADO 1:  {s1}\n")
print(f"RESULTADO 2:  {emp1}")
```

## encapsulamiento

```py
class Persona:

    tipo = "Humano"  #Dato al que pueden acceder
    __sueldo = 2000  #No quiero que accedan a mi cuenta - privado
    _data = "asdf" # variable protegida - no se usa tanto, es de python 2

    def __init__(self, nombre, apellido):
        self.nombre = nombre  #NO me molesta que sepan mi nombre
        self.__apellido = apellido #No quiero que sepan mi apellido

    def __soy_feliz(self): # método privado
        print("No les importa ¬¬")

    def edad(self):
        return 31 #Soy joven aún no miento con mi edad



persona1 = Persona("Nicolas", "Lopez")

print(f"Resultado1: {persona1.tipo}\n")
#print(f"Resultado2: {persona1.__sueldo}\n") # error 
print(f"Resultado3: {persona1.nombre}\n")
#print(f"Resultado4: {persona1.__apellido}\n")
#print(f"Resultado5: {persona1.__soy_feliz()}\n")
print(f"Resultado6: {persona1.edad()}\n")
```

- get y set

se recomienda que todos los datos sean _PRIVADOS_ y que creemos funciones para acceder a ellos

```py
class Jugador:

    def __init__(self, nombre, apellido):

        #Se suelen hacer privados todos los atributos
         self.__nombre = nombre
         self.__apellido = apellido
         self._goles = 23   #Un solo guion bajo no es ni publico ni privado, es protegido, que en la proxima clase lo entenderemos

    #Se generan metodos get PUBLICOS de los atributos que quieres que sean visibles.
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    #Se generan metodos set PUBLICOS de los atributos que quieres que sean visibles y MODIFICABLES
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido


jugador1 = Jugador("Brenda", "Benitez")
print(jugador1.get_apellido())  #Para acceder al apellido
print(jugador1.get_nombre())  #Para acceder al nombre()
jugador1.set_apellido("Gutierrez")  #Para modificar al apellido
jugador1.set_nombre("Ricardo")  #Para acceder al nombre
print(jugador1.get_apellido())  #Para acceder al apellido
print(jugador1.get_nombre())  #Para acceder al nombre
print(jugador1._goles)  #qué pasa con los goles - ERROR!
```



















