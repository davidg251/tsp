import networkx as nx

class Vc:

    k = 0
    matriz = []
    grafo = nx.Graph()

    def crearGrafo(self):

        n = len(self.matriz)
        print n
        for i in range(0,n):
            self.grafo.add_node(i)
            for j in range(0,n):

                if self.matriz[i][j] == 1:
                    self.grafo.add_edge(i,j)
        #print self.grafo.edges()
