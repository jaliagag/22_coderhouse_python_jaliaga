numeros = [1,3,6,9]

while True:
    a = int(input("Escribí un número del 0 al 9: "))
    if a in range (10):
        if a in numeros:
            print("ese número está en la lista")
        else:
            print("ese número no está en la lista")
        break


