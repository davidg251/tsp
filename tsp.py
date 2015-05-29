import networkx as nx
import matplotlib.pyplot as plt

class Tsp:

    grafo = nx.Graph()

    def crearSubGrafo(self,key,key2,key3):

        temp = nx.Graph()

        for i in range(0,6):

            if i == 0:
                temp.add_node(key+str(i)+key3,extremo=True)
                temp.add_node(key2+str(i)+key3,extremo=True)
            elif i == 5:
                temp.add_node(key+str(i)+key3,extremo=True)
                temp.add_node(key2+str(i)+key3,extremo=True)
            else:
                temp.add_node(key+str(i)+key3)
                temp.add_node(key2+str(i)+key3)

            if (i != 0):

                temp.add_edge(key + str(i-1) +key3 , key+str(i)+key3)
                temp.add_edge(key2 + str(i-1)+key3 , key2+str(i)+key3)

            if (i == 2):

                temp.add_edge(key+'2'+key3 , key2+'0'+key3)
                temp.add_edge(key+'0'+key3 , key2+'2'+key3)

            if (i == 5):

                temp.add_edge(key+'3'+key3 , key2+'5'+key3)
                temp.add_edge(key+'5' +key3, key2+'3'+key3)


        self.grafo =  nx.union(self.grafo,temp)


    def anadirNodos(self,k):

        extremos = nx.get_node_attributes(self.grafo, 'extremo')

        for s in extremos:
            if self.grafo.degree(s) == 2:
                #print s
                for i in range(0, k):
                    nodo  = 'a'+ str(i)
                    self.grafo.add_node(nodo);
                    self.grafo.add_edge(nodo,s)
                    #print s,nodo




    def anadirAristas(self,aristas):

        n = len(aristas)

        print n

        for i in range(0,n):

            pos0 = aristas[i][0]
            pos1 = aristas[i][1]
            #print pos0,pos1

            for j in range(0,n-1):

                if ((pos0 == aristas[j+1][0] )or (pos0 == aristas[j+1][1])):

                    if(self.grafo.degree(str(pos0) + '0' + str(i)) > 2 ):

                        self.grafo.add_edge((str(pos0) + '5' + str(i)),(str(pos0) + '5' + str(j+1)) )

                    else:

                        self.grafo.add_edge((str(pos0) + '0' + str(i)),(str(pos0) + '0' + str(j+1)) )
                    break

                if((pos1 == aristas[j+1][0]) or (pos1 == aristas[j+1][1])) :

                    if(self.grafo.degree(str(pos1) + '0' + str(i)) > 2 ):

                        self.grafo.add_edge((str(pos1) + '5' + str(i)) ,(str(pos1) + '5' + str(j+1)) )

                    else:

                        self.grafo.add_edge((str(pos1) + '0' + str(i)),(str(pos1) + '0' + str(j+1)) )
                    break
