# programación orientada a objetos | poo

<https://docs.google.com/presentation/d/1KcPY2Al8QUvI3gomR1DoU2KwMwI-RPn0/edit?usp=sharing&ouid=112228475767659518578&rtpof=true&sd=true>
<https://colab.research.google.com/drive/1Jy7ooc2dOgtf2KwvEUPuAi0wueNU5KWY?usp=sharing>

## pilares

- abstracción: nos permite convertir los datos y funciones en atributos y métodos de un objeto
- encapsulamiento - mantenemos la integridad de los datos, que los datos (atributos?) no sean modificables; nos permite empaquetar en una sola clase (reutilizar)
- herencia: reutilizar - que los objetos se puedan usar en otras clases 
- polimorfismo: dependiendo del contexto, la clase puede actuar de manera distinta

## diagrama de clases (que son los objetos en python)

estructura estática que describe la estructura de un sistema mostrando las claes del sistema, sus atributos, operaciones y larelaciones entre los objetos

- nombre de la clase
  - coche
- atributos
  - color
  - marca
  - modelo
- métodos
  - estacionar()
  - arrancar()
  - parar()

- superclase -- permite la herencia de atributos y métodos a otras clases
- herencia --> clase que tiene características para reutilizarlas en otras clases
- asociación -- : relación semántica entre objetos no relacionados. _pertenece a_ o _está asociado con_ - **una clase usa a otra clase para realizar algo**. están relacionados pero no
  - una persona (clase) usa un auto (otra clase) - no comparten características pero están asociados
- agregación --# : todo y sus partes. cualquier caballo puede estar adentro de una clase pero no todas las clases están por defecto dentro de esta
  - clase coche : sería la clase _TODO_ - objecto contenedor de otros objectos
    - clase motor : la clase _PARTE_ pertene al coche pero es una clase en sí

## cardinalidad de las relaciones

Cardinalidad: indicar el número de objetos que están en la relación; una persona puede tener muchos autos, pero un auto solo tiene un motor

- `..*` -- relación es a muchos objetos
- `1` -- relación solo es a uno
- `0,1` -- a uno o ninguno

- Público: se puede modificar
- Privado: no se puede modificar

1:00:00
