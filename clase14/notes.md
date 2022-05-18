# herencia y polimorfismo

- <https://docs.google.com/presentation/d/1IN40Ae4gC7ig1m04EV5hFyW_FyTG6IKC/edit?usp=sharing&ouid=112228475767659518578&rtpof=true&sd=true>
- <https://drive.google.com/file/d/1FMoN7Xew7t9neFYciby7es0MMMV1oK4p/view?usp=sharing>

crear una clase hija que herada de una clase padre, comparte métodos y atributos - puede _sobreescribir_ los métodos o atributos o definir nuevos

```py
# superclase
class Animal:
  pass

# subclase
class Perro(Animal):
  pass
```

DRY: don't repeat yourself

```py
class Animal:
  def __init__(self, especie, edad):
    self.especie = especie
    self.edad = edad
  def hablar(self):
    pass

  def moverse(self):
    pass

  def __str__(self):
    return f"ESPECIE: {self.especie}, EDAD: {self.edad}"
  def describir(self):
    print(f'soy un animal del tipo: {type(self).__name__}')
```

```py
class Perro(Animal):
  def hablar(self):
    print("guau!")

  def moverse(self):
    print('caminando con 4 patas')

perro1 = Perro("mamífero",11) # la declaramos según la superclase
print(perro1)     # heredada de la subclase
perro1.hablar()   # propia de la subclase  
perro1.moverse()

class Vaca(Animal):
  def hablar(self):
    print("Muuuu!")
  def moverse(self):
    print("caminando con 4 patas")

class Abeja(Animal):
  def hablar(self):
    print("Bzzzz!")
  def moverse(self):
    print("volando")
  def picar(self):
    print("Picar!")

vaca1 = Vaca("milka",12)
vaca1.hablar()

```

### super()

```py
clase Perro(Animal):
# alternativa 1
#  def __init__(self,especie,edad,duenio):
#    self.especie = especie
#    self.edad = edad
#    self.owner = owner
# alternativa 2
  def __init__(self,especie,edad,duenio):
    super().__init(especie,edad)
    self.owner = owner
```

### herencia múltiple

una clase hereda de varias clases padre

```py
class Clase1:
  pass
class Clase2:
  pass
class Clase3(Clase1,Clase2):
  pass
```

MRO: esta función nos devuelve una tupla con el orden de búsqueda de los métodos

```py
print(Clase3.__mro__)
# primero busca el método en la clase3, después en la clase 2 y después en la clase1
```

## polimorfismo

objetos de diferentes clases






