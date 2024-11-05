# Importamos las estructuras de datos necesarias
from cola import Queue
from heap import HeapMin
from pila import Stack

# defino el grafo
class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def insert_vertice(self, personaje):
        nodo = {
            'value': personaje,
            'aristas': [],  
            'visitado': False,  # 'visitado' es para buscar dsp
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, episodios):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            arista = {
                'value': destino,
                'peso': episodios 
            }
            self.elements[pos_origen]['aristas'].append(arista)
            if not self.dirigido:
                arista = {
                    'value': origen,
                    'peso': episodios
                }
                self.elements[pos_destino]['aristas'].append(arista)

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index

    def kruskal(self):
        bosque = []
        aristas = HeapMin()
        
        for nodo in self.elements:
            bosque.append({nodo['value']})
            adjacentes = nodo['aristas']
            for adyacente in adjacentes:
                aristas.arrive([nodo['value'], adyacente['value']], adyacente['peso'])

        min_tree = []
        while len(bosque) > 1 and len(aristas.elements) > 0:
            peso, arista = aristas.atention()
            origen, destino = arista
            origen_conj = next((c for c in bosque if origen in c), None)
            destino_conj = next((c for c in bosque if destino in c), None)

            # uno los que no estan en el mismo conjunto
            if origen_conj != destino_conj:
                min_tree.append((origen, destino, peso))
                bosque.remove(origen_conj)
                bosque.remove(destino_conj)
                bosque.append(origen_conj | destino_conj)

        contiene_yoda = any("Yoda" in conjunto for conjunto in bosque)
        return min_tree, contiene_yoda

    def max_episodios_compartidos(self):
        # Busco el máximo de episodios compartidos entre personajes
        max_episodios = 0
        personajes = None
        for nodo in self.elements:
            for arista in nodo['aristas']:
                if arista['peso'] > max_episodios:
                    max_episodios = arista['peso']
                    personajes = (nodo['value'], arista['value'])
        return max_episodios, personajes


# creo el grafo no dirigido y los pj
grafo = Graph(dirigido=False)
personajes = ['Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-3PO', 'Leia', 
              'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8', 
              'Obi-Wan Kenobi', 'Mace Windu', 'Padmé Amidala', 'Qui-Gon Jinn']

#Inserto los vertices que son los pj
for personaje in personajes:
    grafo.insert_vertice(personaje)

# Inserto aristas que son la cant. de episodios compartidos 
grafo.insert_arista('Luke Skywalker', 'Darth Vader', 4)
grafo.insert_arista('Luke Skywalker', 'Yoda', 2)
grafo.insert_arista('Leia', 'Han Solo', 3)
grafo.insert_arista('Chewbacca', 'Han Solo', 3)
grafo.insert_arista('Leia', 'C-3PO', 5)
grafo.insert_arista('Rey', 'Kylo Ren', 3)
grafo.insert_arista('R2-D2', 'Luke Skywalker', 3)
grafo.insert_arista('Luke Skywalker', 'Obi-Wan Kenobi', 4)
grafo.insert_arista('Darth Vader', 'Palpatine', 6)
grafo.insert_arista('Yoda', 'Obi-Wan Kenobi', 3)
grafo.insert_arista('Leia', 'Han Solo', 3)
grafo.insert_arista('Padmé Amidala', 'Anakin Skywalker', 5)

# Busco el arbol de expansion minima y pregunto si existe Yoda
arbol_expansion, contiene_yoda = grafo.kruskal()
print("Árbol de expansión mínimo:", arbol_expansion)
print("Contiene a Yoda:", contiene_yoda)

# Obtengo num maximo de episodios compartidos y los pj involucrados
max_episodios, personajes = grafo.max_episodios_compartidos()
print("Maximo de episodios compartidos:", max_episodios)
print("Personajes:", personajes)
