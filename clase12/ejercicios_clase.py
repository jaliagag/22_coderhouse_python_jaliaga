#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tradicionalmente

brand = 'FORD'
model = 'mustang'
color = 'Rojo'
plate = 'AEAEA'
year = 1965

def mostrarVehiculo(a,b,c,d,e):
    print('-----------------')
    print(f'marca: {a}')
    print(f'modelo: {b}')
    print(f'color: {c}')
    print(f'patente: {d}')
    print(f'año: {e}')
    print('-----------------')

#print('Tradicionalmente:')
#mostrarVehiculo(brand,model,color,plate,year)

# Prgramación estructurada

#clientes = [
#    {'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
#    {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'} 
#]

def mostrarCliente(client,nid):
    for c in client:
        if (nid == c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return
    print('Cliente no encontrado')

#mostrarCliente(clientes, '11111111B')

def borrarCliente(clientes,nid):
    for i,c in enumerate(clientes):
        if (nid == c['dni']):
            del(clientes[i])
            print(str(c),"> BORRADO")
            return
    print('Cliente no encontrado')
    
#print('Antes de borrrar:')
#print(clientes)
#print('Borrando...')
#borrarCliente(clientes,'11111111A')
#print('Resultado:')
#print(clientes)

class Client:
    # atributos
    def __init__(self, dni, name, lastname):
        self.dni = dni
        self.name = name
        self.lastname = lastname
    # funcionalidad - métodos
    def __str__(self):
        return '{} {}'.format(self.name,self.lastname)

class Company:
    def __init__(self, clients=[]):
        self.clients = clients

    def showClient(self,dni=None):
        for c in self.clients:
            if c.dni == dni:
                print(c)
                return
        print('Cliente no encontrado')
    
    def deleteClient(self,dni=None):
        for i,c in enumerate(self.clients):
            if c.dni == dni:
                del(self.clients[i])
                print(str(c),'> BORRADO')
                return
        print('Cliente no encontrado')

# creamos una par de clientes
daniel = Client(name='Daniel', lastname='Lalicata', dni='12345678')
martin = Client('987654321','Samez','Martin')

# creamos una empresa
apple = Company(clients=[daniel,martin])

# mostramos los clients
print(apple.clients)
# este print nos muestra la ubicación de los objetos en memoria
apple.showClient('123456780')
apple.showClient('12345678')



