import os
import pickle
import random


class Operacion:
    def __init__(self, id, descr, imp, tip, zona):
        self.id = id
        self.descripcion = descr
        self.importe = imp
        self.tipo = tip
        self.zona = zona


def cargar_vector(vector, n):
    for i in range(n):
        id = random.randint(1000, 9999)
        descr = "Operación " + str(i)
        imp = random.uniform(1500, 15000)
        tipo = random.randint(1, 15)
        zona = random.randrange(20)
        operacion = Operacion(id, descr, imp, tipo, zona)
        add_in_order(vector, operacion)
    print("El vector se cargó correctamente...")


def add_in_order(vector, operacion):
    izq, der = 0, len(vector) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if vector[med].id == operacion.id:
            pos = med
            break

        if operacion.id < vector[med].id:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [operacion]






def mostrar_vector(vector, z):
    print(encabezado(), end="")
    for registro in vector:
        if registro.zona >= z:
            print(to_string(registro), end='')


def encabezado():
    cad = '{}\n'.format('-' * 55)
    cad += '| {:^5} | {:^12} | {:^10} | {:^5} | {:^5} |\n'
    cad += '{}\n'.format('-' * 55)
    return cad.format('Id', 'Descripción', 'Importe', 'Tipo', 'Zona')


def to_string(operacion):
    cad = '| {:^5} | {:^12} | {:^10.2f} | {:^5} | {:^5} |\n'
    cad += '{}\n'.format('-' * 55)
    return cad.format(operacion.id, operacion.descripcion, operacion.importe, operacion.tipo, operacion.zona)


def crear_matriz_conteo(vector):
    matriz = [[0] * 20 for i in range(15)]
    for registro in vector:
        f = registro.tipo - 1
        c = registro.zona
        matriz[f][c] += 1
    return matriz


def mostrar_matriz(matriz, li, ld):
    cad = 'Se realizaron {:>5} operaciones para el tipo de operacion {:>5} y zona geográfca {:>5}'
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] >= li and matriz[f][c] <= ld:
                print(cad.format(matriz[f][c], f + 1, c))


def calcular_promedio(vector):
    acum = promedio = 0
    cont = len(vector)
    for operacion in vector:
        acum += operacion.importe
    if cont != 0:
        promedio = acum / cont

    return promedio



def crear_archivo(vector, importe, nombre_archivo):
    m = open(nombre_archivo, 'wb')
    for operacion in vector:
        if operacion.importe > importe:
            pickle.dump(operacion, m)
    m.close()
    print("El archivo se creó correctamente...")



def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print('No existe un archivo llamado {}'.format(nombre_archivo))
        return
    cont = 0
    m = open(nombre_archivo, 'rb')
    size = os.path.getsize(nombre_archivo)
    print(encabezado(), end="")
    while m.tell() < size:
        cont += 1
        operacion = pickle.load(m)
        print(to_string(operacion), end='')
    print("Se mostraron ", cont, " registros")
    m.close()


def validar_mayor_que(minimo, mensaje='Cargar un numero: '):
    numero = minimo
    while numero <= minimo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print('Error!!! El valor debe ser mayor a {}'.format(minimo))
    return numero


def validar_entre(minimo, maximo, mensaje='Cargar un numero: '):
    numero = minimo - 1
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje))
        if numero < minimo or numero > maximo:
            print("Error!!! El valor debe estar entre ", minimo, " y ", maximo)
    return numero
