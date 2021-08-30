import xml.etree.ElementTree as ET
import math
import os
from tkinter.filedialog import askopenfilename
from graphviz import Graph
#begins code
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
        self.size = 0

    def add(self, dato):
        self.size += 1
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

    def pop(self):
        if self.size>0:
            nodoAux = self.cabecera
            if self.size == 1:
                self.size -= 1
                return nodoAux.dato
            else:
                while nodoAux.siguiente != self.ultimo:
                    nodoAux = nodoAux.siguiente
                nodoAux2 = self.ultimo
                nodoAux.siguiente = None
                self.ultimo = nodoAux
                self.size -= 1
                return nodoAux2.dato
        else:
            return None

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
                        cA.acumulado = int(acumulado)
                        cA.predecesor = celdaAux
                        cp.add(cA)

            if (celdaAux.posicionY+1)<=self.dimensionY:
                celdaAb = celda(celdaAux.posicionX,celdaAux.posicionY+1, 0)
                cA = self.buscar(celdaAb)
                if analizados.buscarCelda(cA) != True:
                    acumulado = float(celdaAux.acumulado) + float(cA.valor)
                    if acumulado < cA.acumulado:
                        cp.eliminar(cA)
                        cA.acumulado = int(acumulado)
                        cA.predecesor = celdaAux
                        cp.add(cA)

            if (celdaAux.posicionX-1)>0:
                celdaIz = celda(celdaAux.posicionX-1,celdaAux.posicionY, 0)
                cA = self.buscar(celdaIz)
                if analizados.buscarCelda(cA) != True:
                    acumulado = float(celdaAux.acumulado) + float(cA.valor)
                    if acumulado < cA.acumulado:
                        cp.eliminar(cA)
                        cA.acumulado = int(acumulado)
                        cA.predecesor = celdaAux
                        cp.add(cA)

            if (celdaAux.posicionX+1)<=self.dimensionX:
                celdaDer = celda(celdaAux.posicionX+1,celdaAux.posicionY, 0)
                cA = self.buscar(celdaDer)
                if analizados.buscarCelda(cA) != True:
                    acumulado = float(celdaAux.acumulado) + float(cA.valor)
                    if acumulado < cA.acumulado:
                        cp.eliminar(cA)
                        cA.acumulado = int(acumulado)
                        cA.predecesor = celdaAux
                        cp.add(cA)
            analizados.add(celdaAux)

    def Ruta(self, final):
        celdaFinal = final
        celdaAux = final
        recorrido = listaSimple()
        recorrido.add(celdaAux)
        while celdaAux.predecesor != None:
            celdaAux = celdaAux.predecesor
            recorrido.add(celdaAux)
        return recorrido

    def imprimirRuta(self, recorrido):
        print('\nLa ruta con menor consumo de combustible es:')
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
                        if subsubelem.tag == 'n':
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

def escribirArchivo(ruta, contenido):
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    print('\narchivo escrito:')
    print(ruta)
    archivo.close()

def crearXml(nombre,dimensionX,dimensionY,posicionInicioX,posicionInicioY,posicionFinX,posicionFinY,combustible, camino):
    inicio = '<terreno nombre="'+nombre+'">\n  <dimension>\n    <n>'+dimensionX+'</n>\n    <m>'+dimensionY+'</m>\n  </dimension>\n  <posicioninicio>\n    <x>'+posicionInicioX+'</x>\n    <y>'+posicionInicioY+'</y>\n  </posicioninicio>\n  <posicionfin>\n    <x>'+posicionFinX+'</x>\n    <y>'+posicionFinY+'</y>\n  </posicionfin>\n  <combustible>'+combustible+'</combustible>'
    celdaAux = camino.pop()
    while celdaAux != None:
        inicio += '\n  <posicion x="'+str(celdaAux.posicionX)+'" y="'+str(celdaAux.posicionY)+'">'+str(celdaAux.valor)+'</posicion>'
        celdaAux = camino.pop()
    fin = '\n</terreno>'
    return inicio + fin

def crearGrafica(nombre, matriz):
    dot = Graph(name=nombre)
    dot.graph_attr['rankdir'] = 'LR'
    nodoAux = matriz.columnas.cabecera
    i = 1
    while nodoAux != None:
        with dot.subgraph(name='sub_'+str(i)) as b:
            nodoAux1 = nodoAux.dato.cabecera
            contador = 0
            while nodoAux1 != None:
                contador += 1
                b.node(str(i)+str(contador),str(nodoAux1.dato.valor))
                if contador > 1:
                    b.edge(str(i)+str(contador-1), str(i)+str(contador))
                    if i > 1:
                        b.edge(str(i)+str(contador-1), str(i-1)+str(contador-1),_attributes={'constraint': 'false'})
                        if contador == nodoAux.dato.size:
                            b.edge(str(i)+str(contador), str(i-1)+str(contador),_attributes={'constraint': 'false'})
                nodoAux1 = nodoAux1.siguiente
            nodoAux = nodoAux.siguiente
            i += 1
    dot.render(nombre, format='png', view=True)

def menu():
    terrenos =''
    terreno = ''
    recorrido = ''
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
            print('Por favor cargue un archivo para analizar :) \n')
            continue

        if option == 1:
            print('Cargar Archivo')
            try:
                terrenos = CargarArchivos()
                print('\nCargando Archivos...')
            except Exception as e:
                print('archivo erroneo')

        elif option == 2:
            print('Procesar archivo')
            if terrenos != '':
                try:
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
                    print('Analizando terreno: '+terreno.nombre)
                    print('Posicion de Inicio: '+str(terreno.posicionInicioX)+','+str(terreno.posicionInicioY))
                    print('Posicion final: '+str(terreno.posicionFinX)+','+str(terreno.posicionFinY))
                    matrizTerreno.imprimir()
                    recorrido = matrizTerreno.Ruta(matrizTerreno.buscar(celdaFinal))
                    matrizTerreno.imprimirRuta(recorrido)
                    print('\nCantidad de combustible necesaria: '+str(matrizTerreno.buscar(celdaFinal).acumulado))
                except Exception as e:
                    print('')
            else:
                print('Opcion no válida, por favor intente de nuevo\n')

        elif option == 3:
            print('Escribir archivo salida')
            if terrenos != '':
                try:
                    print('\nObteniendo terrenos...\n')
                    print('\nLista de Terrenos:\n')
                    terrenos.imprimir()
                    var = input('\nIngrese el nombre del terreno que desea procesar\n')
                    terreno = terrenos.buscar(var)
                    matrizTerreno = terreno.matriz
                    celdaInicio = celda(terreno.posicionInicioX,terreno.posicionInicioY,0)
                    matrizTerreno.obtenerRuta(matrizTerreno.buscar(celdaInicio))
                    celdaFinal = celda(terreno.posicionFinX,terreno.posicionFinY,0)
                    recorrido = matrizTerreno.Ruta(matrizTerreno.buscar(celdaFinal))
                    contenido = crearXml(terreno.nombre, str(terreno.dimensionX), str(terreno.dimensionY), str(terreno.posicionInicioX), str(terreno.posicionInicioY), str(terreno.posicionFinX), str(terreno.posicionFinY), str(matrizTerreno.buscar(celdaFinal).acumulado),recorrido)
                    variable = int(input(' 1. Escribir ruta\n 2. Guardar en la carpeta del proyecto\nEscoja la opcion deseada:'))
                    if variable == 1:
                        name = input('Escriba la ruta para guardar el archivo, por  favor incluya nombre y extension\n')
                        escribirArchivo(name,contenido)
                    elif variable == 2:
                        escribirArchivo(terreno.nombre+'.xml',contenido)
                    else:
                        print('opcion no valida, por favor intente de nuevo :) ')
                except Exception as e:
                    print('')
            else:
                print('Por favor cargue un archivo para analizar :) \n')
        elif option == 4:
            print('Mostrar datos del estudiante:')
            print('> Rony Omar Miguel Lopez\n> 201905750\n> Introduccion a la Programacion y Computacion seccion '"A"'\n> Ingenieria en Ciencias y Sistemas\n> 4to Semestre\n')
        elif option == 5:
            print('Generar grafica')
            if terrenos != '':
                if terrenos != '':
                    try:
                        print('\nObteniendo terrenos...\n')
                        print('\nLista de Terrenos:\n')
                        terrenos.imprimir()
                        var = input('\nIngrese el nombre del terreno que desea graficar\n')
                        terreno = terrenos.buscar(var)
                        matrizTerreno = terreno.matriz
                        matrizAux = matrizTerreno
                        print("Creando grafica...")
                        contenido = crearGrafica(terreno.nombre, matrizAux)
                    except Exception as e:
                        print('')
                else:
                    print('Por favor cargue un archivo para analizar :) \n')
            else:
                print('Por favor cargue un archivo para analizar :) \n')
        elif option == 6:
            print('Hasta la proxima, byeeee :)')
            break
        else:
            print('Opcion no válida, por favor intente de nuevo\n')


if __name__ == '__main__':
    menu()
