import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

class terreno:
    def __init__(self, nombre, dimensionX, dimensionY, posicionInicioX, posicionInicioY, posicionFinX, posicionFinY, Matriz):
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


class celda:
    def __init__(self, posicionX, posicionY, valor):
        self.posicionX = int(posicionX)
        self.posicionY = int(posicionY)
        self.valor = valor
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

        self.filas = listaSimple()
        i = 1
        while i <= self.dimensionX:
            fila = listaSimple()
            j = 1
            while j <= self.dimensionY:
                print('creando posicion '+str(i)+str(j))
                posicion = 'pos'+str(i)+str(j)
                columna = nodoLista(posicion)
                fila.add(columna)
                j += 1
            self.filas.add(fila)
            i += 1


    def add(self, celda):
        print('agregando celda '+str(celda.posicionX)+str(celda.posicionY))
        if celda.posicionX == 1:
            listaAux = self.filas.cabecera.dato
            print(type(listaAux))
            i = 1
            nodoAux = listaAux.cabecera
            while i < celda.posicionY:
                nodoAux = nodoAux.siguiente
                print(type(nodoAux))
                i += 1
            nodoAux.dato = celda
        else:
            print('error en else')
            nodoAux = self.filas.cabecera
            i = 1
            while i < celda.posicionX:
                nodoAux = nodoAux.siguiente
                i += 1
            listaAux = nodoAux.dato
            print(type(listaAux))
            nodoProv = listaAux.cabecera
            j = 1
            while j < celda.posicionY:
                nodoProv = nodoProv.siguiente
                print(type(nodoProv))
                j +=1
            nodoProv.dato = celda




if __name__ == '__main__':
    f = askopenfilename()
    tree = ET.parse(f)
    root = tree.getroot()

    terrenos = listaSimple()
    for elem in root:
        name = elem.attrib.get('nombre')
        print(name)
        for subelem in elem:
            atributo = subelem
            print(atributo.tag)
            if atributo.tag == 'dimension':
                for subsubelem in subelem:
                    if subsubelem.tag == 'm':
                        dimensionX = subsubelem.text
                        print('dimension en X'+dimensionX)
                    else:
                        dimensionY = subsubelem.text
                        print('dimension en Y'+dimensionY)
                matrizLista = matriz(dimensionX,dimensionY)
            elif atributo.tag == 'posicioninicio':
                for subsubelem in subelem:
                    if subsubelem.tag == 'x':
                        posicionInicioX = subsubelem.text
                        print('Posinicio en x'+posicionInicioX)
                    else:
                        posicionInicioY = subsubelem.text
                        print('Posinicio en Y'+posicionInicioY)
            elif atributo.tag == 'posicionfin':
                for subsubelem in subelem:
                    if subsubelem.tag == 'x':
                        posicionFinX = subsubelem.text
                        print('PosFin en X'+posicionFinX)
                    else:
                        posicionFinY = subsubelem.text
                        print('PosFin en Y'+posicionFinY)
            elif atributo.tag == 'posicion':
                x = atributo.get('x')
                y = atributo.get('y')
                valor = atributo.text
                nuevaCelda = celda(x,y,valor)
                matrizLista.add(nuevaCelda)

        terrenoNuevo = terreno(name, dimensionX,dimensionY,  posicionInicioX, posicionInicioY, posicionFinX, posicionFinY, matrizLista)
        terrenos.add(terrenoNuevo)

    terrenos.imprimir()
