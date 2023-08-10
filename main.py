from utilidades import *

"""
Una compañía de servicios agropecuarios desea desarrollar un programa Python que le permita gestionar la información 
de cada operación agrícola realizada. Por cada operación se dispone de la siguiente información: número de identificación
 (un entero), descripción de la operación (una cadena), el importe a facturar por esa operación (un float), el tipo de 
 operación (un entero entre 1 y 15, por ejemplo: 0: riego, 1: cosecha, etc.), y un campo para indicar la zona geográfica 
 donde se aplica (un valor entre 0 y 19, por ejemplo: 0: centro de Buenos Aires, 1: Sur de Córdoba, etc.) Se pide definir
  el tipo registro Operación con los campos pedidos, y desarrollar un programa en Python controlado por un menú de 
  opciones que permita gestionar las siguientes tareas:

1- Cargar un arreglo de registros con los datos de n operaciones. Valide los campos que sea necesaraio. 
Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe
 ser manual, y si la hace automática entonces TODA debe ser automática). El arreglo debe crearse de forma que siempre 
 quede ordenado de menor a mayor por código de identificación. Para esto debe utilizar el algoritmo  inserción ordenada 
 con búsqueda binaria. Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y 
 ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el contenido completo del vector a razón de un registro por línea, pero solo de los registros cuya zona
 geográfica sea mayor o igual al valor z que se carga por teclado.

3- A partir del vector de registros, genere una matriz para contar cuántas operaciones de cada tipo se hicieron en 
cada posible zona (matriz de conteo de 15 * 20). Al finalizar, muestre el contenido de la misma pero solo muestre los
 contadores cuyos valores estén comprendidos entre los números v1 y v2 que se cargan por teclado.

4- Genere un archivo que contenga los datos del arreglo, pero solo almacene los registros cuyo importe a facturar sea 
mayor al importe promedio de todos los registros del vector.

5- Muestre el contenido del archivo a razón de un registro por línea. Al final del listado muestre una línea adicional
indicando la cantidad de registros que se mostraron.
"""

def menu():
    cad = 'Menu de Opciones\n' \
          '==============================================\n' \
          '1 ----- Cargar Vector de Operaciones\n' \
          '2 ----- Mostrar Vector de Operaciones\n' \
          '3 ----- Crear matriz de conteo\n' \
          '4 ----- Crear Archivo de Operaciones con filtro\n' \
          '5 ----- Mostrar archivo\n' \
          '0 ----- Salir\n' \
          'Ingrese su opcion: '
    return int(input(cad))


def principal():
    operaciones = []
    nombre_archivo = 'operaciones.dat'
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = validar_mayor_que(0, "Ingrese la cantidad de operaciones a cargar: ")
            cargar_vector(operaciones, n)
        elif len(operaciones) > 0:
            if opcion == 2:
                z = validar_entre(0, 19, "Ingrese la zona geográfica mínima para mostrar(entre 0 y 19): ")
                mostrar_vector(operaciones, z)
            elif opcion == 3:
                v1 = validar_mayor_que(-1, "Ingrese el limite izquierdo para mostrar: ")
                v2 = validar_mayor_que(v1, "Ingrese el limite derecho para mostrar: ")
                matriz = crear_matriz_conteo(operaciones)
                mostrar_matriz(matriz, v1, v2)
            elif opcion == 4:
                importe_promedio = calcular_promedio(operaciones)
                crear_archivo(operaciones, importe_promedio, nombre_archivo)
            elif opcion == 5:
                leer_archivo(nombre_archivo)
        else:
            print('Primero debe cargar el arreglo con operaciones a procesar...')


if __name__ == '__main__':
    principal()
