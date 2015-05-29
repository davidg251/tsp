from tsp import Tsp
from vc import Vc
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Controlador:

    vcObj = Vc()
    tspObj = Tsp()

    def leerArchivo(self,ruta):

        fichero = open(ruta,'r')

        lista = fichero.readlines()
        n = int( lista[0] )
        self.vcObj.k = int( lista[n+1] )

        incidencia = []

        for i in range(1,n+1):
            incidencia.append( lista[i].split(" ",n) )
            for j in range(0,n):
                incidencia[i-1][j] = int( incidencia[i-1][j])

        self.vcObj.matriz = incidencia
        fichero.close()


    def ejecutarReduccion(self):

        edges = self.vcObj.grafo.edges()
        n = len(edges)
        #print n

        for i in range(0,n):

            self.tspObj.crearSubGrafo(str(edges[i][0]), str(edges[i][1]) , str(i))

        edges = self.vcObj.grafo.edges()
        self.tspObj.anadirAristas(edges)
        self.tspObj.anadirNodos(self.vcObj.k)
        #self.tspObj.conectarNodos()

        t = nx.adjacency_matrix(self.tspObj.grafo)

        m = t.todense()
        #print len(m)
        nu = str ( len(m) )
        np.savetxt('salida.data',m,header=nu,fmt='%0i',comments='')


    def crearVertexCover(self):

        self.vcObj.crearGrafo()


    def mostrarVertexCover(self):

        plt.clf()
        g = self.vcObj.grafo
        nx.draw_graphviz(g,prog='neato',with_labels="True")
        plt.savefig("vc.png", format="PNG")

    def mostrarReduccion(self):

        plt.clf()
        g = self.tspObj.grafo
        nx.draw_graphviz(g,prog='neato',with_labels="True")
        plt.savefig("tsp.png", format="PNG")
