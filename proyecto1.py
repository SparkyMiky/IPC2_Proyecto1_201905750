import xml.etree.ElementTree as ET
import math
import os
from tkinter.filedialog import askopenfilename

class terreno:
    def __init__(self, nombre, dimensionX, dimensionY, posicionInicioX, posicionInicioY, posicionFinX, posicionFinY, matriz):
        self.nombre = nombre
        self.dimensionX = dimensionX
        self.dimensionY = dimensionY
        self.posicionInicioX = posicionInicioX
        self.posicionInicioY = posicionInicioY
        self.posicionFinX = posicionFinX
        self.posicionFinY = posicionFinY
        self.matriz = matriz
class nodoLista:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def getDato(self):
        return self.dato

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, nodoLista):
        self.siguiente = nodoLista
class listaSimple:
    def __init__(self):
        self.cabecera = None
        self.ultimo = None
        self.siguiente = None

    def add(self, dato):
        nodoAux = nodoLista(dato)
        if self.cabecera == None:
            self.cabecera = nodoAux
            self.ultimo = nodoAux
        else:
            self.ultimo.siguiente = nodoAux
            self.ultimo = nodoAux

    def imprimir(self):
        nodoAux = self.cabecera
        while nodoAux != None:
            print(nodoAux.dato.nombre)
            nodoAux = nodoAux.siguiente

    def imprimirCeldas(self):
        nodoAux = self.cabecera
        while nodoAux != None:
            print(nodoAux.dato.valor)
            nodoAux = nodoAux.siguiente

    def buscar(self, nombre):
        nodoAux = self.cabecera
        while nodoAux != None:
            if(nodoAux.dato.nombre == nombre):
                print('\nTerreno encontrado\n')
                return nodoAux. dato
                break
            else:
                print('buscando '+nombre)
            nodoAux = nodoAux.siguiente
        if nodoAux == None:
            print('\nTerreno no encontrado, valide sus datos\n')

    def buscarCelda(self, celda):
        nodoAux = self.cabecera
        while nodoAux != None:
            if(nodoAux.dato == celda):
                return True
                break
            else:
                nodoAux = nodoAux.siguiente
        if nodoAux == None:
            return False

    def buscarMinimo(self):
        nodoAux = self.cabecera
        minimo = nodoAux.dato.valor
        celda = nodoAux.dato
        while nodoAux != None:
            if nodoAux.dato.valor < minimo:
                minimo = nodoAux.dato.valor
                celda = nodoAux.dato
            nodoAux = nodoAux.siguiente
        return celda

class colaPrioridad():
    def __init__(self):
        self.cabecera = None
        self.size = 0

    def add(self, celda):
        self.size += 1
        nodoAux1 = nodoCola(celda)
        if self.cabecera == None:
            self.cabecera = nodoAux1
        else:
            nodoAux = self.cabecera
            while nodoAux.siguiente != None:
                if nodoAux.siguiente.celda.acumulado > celda.acumulado:
                    nodoAux1.siguiente = nodoAux.siguiente
                    nodoAux.siguiente= nodoAux1
                    break
                nodoAux = nodoAux.siguiente
            nodoAux.siguiente = nodoAux1

    def pop(self):
        self.size -= 1
        nodoAux = self.cabecera
        self.cabecera = nodoAux.siguiente
        return nodoAux.celda

    def eliminar(self, celda):
        if self.size > 0:
            nodoAux = self.cabecera
            if self.cabecera.celda == celda:
                self.size -= 1
                self.cabecera = self.cabecera.siguiente
            else:
                while nodoAux.siguiente != None:
                    if nodoAux.siguiente.celda == celda:
                        self.size -= 1
                        nodoAux2 = nodoAux.siguiente
                        if nodoAux2.siguiente == None:
                            nodoAux.siguiente = None
                        else:
                            nodoAux.siguiente = nodoAux2.siguiente
                        break
                    nodoAux = nodoAux.siguiente

    def imprimir(self):
        nodoAux = self.cabecera
        while nodoAux != None:
            print(nodoAux.celda.valor)
            nodoAux = nodoAux.siguiente
class nodoCola():
    def __init__(self, celda):
        self.celda = celda
        self.siguiente = None

class celda:
    def __init__(self, posicionX, posicionY, valor):
        self.posicionX = int(posicionX)
        self.posicionY = int(posicionY)
        self.valor = valor
        self.acumulado = math.inf
        self.predecesor = None
class nodoMatriz:

    def __init__ (self, celda, posicionX, posicionY):
        self.celda = celda
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.siguiente = None
class matriz:
    def __init__(self, dimensionX, dimensionY):
        self.dimensionX = int(dimensionX)
        self.dimensionY = int(dimensionY)

        self.columnas = listaSimple()
        j = 1
        while j <= self.dimensionY:
            columna = listaSimple()
            i = 1
            while i <= self.dimensionX:
                posicion = 'pos'+str(i)+str(j)
                nodo = nodoLista(posicion)
                columna.add(nodo)
                i += 1
            self.columnas.add(columna)
            j += 1

    def imprimir(self):
        nodoAux = self.columnas.cabecera
        while nodoAux != None:
            print('')
            nodoAux2 = nodoAux.dato.cabecera
            while nodoAux2 != None:
                print(nodoAux2.dato.valor, end=" | ")
                nodoAux2 = nodoAux2.siguiente
            nodoAux = nodoAux.siguiente
        print('')

    def add(self, celda):
        if celda.posicionY == 1:
            listaAux = self.columnas.cabecera.dato
            i = 1
            nodoAux = listaAux.cabecera
            while i < celda.posicionX:
                nodoAux = nodoAux.siguiente
                i += 1
            nodoAux.dato = celda
        else:
            nodoAux = self.columnas.cabecera
            i = 1
            while i < celda.posicionY:
                nodoAux = nodoAux.siguiente
                i += 1
            listaAux = nodoAux.dato
            nodoProv = listaAux.cabecera
            j = 1
            while j < celda.posicionX:
                nodoProv = nodoProv.siguiente
                j +=1
            nodoProv.dato = celda

    def buscar(self, celda):
        nodoAux = self.columnas.cabecera
        nodoAux2 = nodoAux.dato.cabecera
        while nodoAux2.dato.posicionY != celda.posicionY:
            nodoAux = nodoAux.siguiente
            nodoAux2 = nodoAux.dato.cabecera
        while nodoAux2.dato.posicionX != celda.posicionX:
            nodoAux2 = nodoAux2.siguiente
        return nodoAux2.dato

    def obtenerRuta(self, inicio):
        cp = colaPrioridad()
        analizados = listaSimple()
        celdaInicio = inicio
        celdaInicio.acumulado = celdaInicio.valor
        cp.add(celdaInicio)
        while cp.size != 0:
            celdaAux = cp.pop()
            celdaAr = None
            celdaAb = None
            celdaIz = None
            celdaDer = None
            if (celdaAux.posicionY-1)>0:
                celdaAr = celda(celdaAux.posicionX,celdaAux.posicionY-1, 0)
                cA = self.buscar(celdaAr)
                if analizados.buscarCelda(cA) != True:
                    acumulado = float(celdaAux.acumulado) + float(cA.valor)
                    if acumulado < cA.acumulado:
                        cp.eliminar(cA)
                        cA.acumulado = acumulado
                        cA.predecesor = celdaAux
                        cp.add(cA)

            if (celdaAux.posicionY+1)<=self.dimensionY:
                celdaAb = celda(celdaAux.posicionX,celdaAux.posicionY+1, 0)
                cA = self.buscar(celdaAb)
                if analizados.buscarCelda(cA) != True:
                    acumulado = float(celdaAux.acumulado) + float(cA.valor)
                    if acumulado < cA.acumulado:
                        cp.eliminar(cA)
                        cA.acumulado = acumulado
                        cA.predecesor = celdaAux
                        cp.add(cA)

            if (celdaAux.posicionX-1)>0:
                celdaIz = celda(celdaAux.posicionX-1,celdaAux.posicionY, 0)
                cA = self.buscar(celdaIz)
                if analizados.buscarCelda(cA) != True:
                    acumulado = float(celdaAux.acumulado) + float(cA.valor)
                    if acumulado < cA.acumulado:
                        cp.eliminar(cA)
                        cA.acumulado = acumulado
                        cA.predecesor = celdaAux
                        cp.add(cA)

            if (celdaAux.posicionX+1)<=self.dimensionX:
                celdaDer = celda(celdaAux.posicionX+1,celdaAux.posicionY, 0)
                cA = self.buscar(celdaDer)
                if analizados.buscarCelda(cA) != True:
                    acumulado = float(celdaAux.acumulado) + float(cA.valor)
                    if acumulado < cA.acumulado:
                        cp.eliminar(cA)
                        cA.acumulado = acumulado
                        cA.predecesor = celdaAux
                        cp.add(cA)
            analizados.add(celdaAux)

    def imprimirRuta(self, final):
        celdaFinal = final
        celdaAux = final
        recorrido = listaSimple()
        recorrido.add(celdaAux)
        while celdaAux.predecesor != None:
            celdaAux = celdaAux.predecesor
            recorrido.add(celdaAux)

        print('\nLa ruta mas corta es:')
        nodoAux = self.columnas.cabecera
        while nodoAux != None:
            print('')
            nodoAux2 = nodoAux.dato.cabecera
            while nodoAux2 != None:
                if recorrido.buscarCelda(nodoAux2.dato):
                    print('#', end=" | ")
                else:
                    print('.', end=" | ")
                nodoAux2 = nodoAux2.siguiente
            nodoAux = nodoAux.siguiente
        print('')


def CargarArchivos():
    f = askopenfilename()
    print('Analizando archivo...')
    root, extension = os.path.splitext(f)
    if extension == '.xml':
        tree = ET.parse(f)
        root = tree.getroot()

        terrenos = listaSimple()
        for elem in root:
            name = elem.attrib.get('nombre')
            for subelem in elem:
                atributo = subelem
                if atributo.tag == 'dimension':
                    for subsubelem in subelem:
                        if subsubelem.tag == 'm':
                            dimensionX = subsubelem.text
                        else:
                            dimensionY = subsubelem.text
                    matrizLista = matriz(dimensionX,dimensionY)
                elif atributo.tag == 'posicioninicio':
                    for subsubelem in subelem:
                        if subsubelem.tag == 'x':
                            posicionInicioX = subsubelem.text
                        else:
                            posicionInicioY = subsubelem.text
                elif atributo.tag == 'posicionfin':
                    for subsubelem in subelem:
                        if subsubelem.tag == 'x':
                            posicionFinX = subsubelem.text
                        else:
                            posicionFinY = subsubelem.text
                elif atributo.tag == 'posicion':
                    x = atributo.get('x')
                    y = atributo.get('y')
                    valor = atributo.text
                    nuevaCelda = celda(x,y,valor)
                    matrizLista.add(nuevaCelda)
            terrenoNuevo = terreno(name, dimensionX,dimensionY,  posicionInicioX, posicionInicioY, posicionFinX, posicionFinY, matrizLista)
            terrenos.add(terrenoNuevo)
        return terrenos
    else:
        print('fallo al cargar archivo, por favor intente de nuevo')


def menu():
    terrenos =''
    terreno = ''
    while True:
        print('\nMenu Principal:')
        print('      1. Cargar Archivo')
        print('      2. Procesar archivo')
        print('      3. Escribir archivo salida')
        print('      4. Mostar datos del EStudiante')
        print('      5. Generar Grafica')
        print('      6. Salida')
        try:
            option = int(input('Ingrese una opcion\n'))
        except Exception as e:
            print('Opcion invalida')
            continue

        if option == 1:
            try:
                terrenos = CargarArchivos()
                print('\nCargando Archivos...')
            except Exception as e:
                print('archivo erroneo')

        elif option == 2:
            if terrenos != '':
                print('\nProcesando archivo\n')
                print('\nObteniendo terrenos...\n')
                print('\nLista de Terrenos:\n')
                terrenos.imprimir()
                var = input('\nIngrese el nombre del terreno que desea procesar\n')
                terreno = terrenos.buscar(var)
                matrizTerreno = terreno.matriz
                celdaInicio = celda(terreno.posicionInicioX,terreno.posicionInicioY,0)
                celdaFinal = celda(terreno.posicionFinX,terreno.posicionFinY,0)
                matrizTerreno.obtenerRuta(matrizTerreno.buscar(celdaInicio))
                matrizTerreno.imprimir()
                matrizTerreno.imprimirRuta(matrizTerreno.buscar(celdaFinal))
            else:
                print('Por favor cargue un archivo para analizar :) \n')

        elif option == 3:
            if terrenos != '':
                print('Working on it')
            else:
                print('Por favor cargue un archivo para analizar :) \n')
        elif option == 4:
            print('> Rony Omar Miguel Lopez\n> 201905750\n> Introduccion a la Programacion y Computacion seccion '"A"'\n> Ingenieria en Ciencias y Sistemas\n> 4to Semestre\n')
        elif option == 5:
            if terrenos != '':
                print('Working on it')
            else:
                print('Por favor cargue un archivo para analizar :) \n')
        elif option == 6:
            print('Hasta la proxima, byeeee :)')
            break
        else:
            print('Opcion no válida, por favor intente de nuevo\n')


if __name__ == '__main__':
    menu()
