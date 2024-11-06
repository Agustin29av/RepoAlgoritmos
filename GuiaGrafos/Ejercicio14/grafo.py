from cola import Queue
from heap import HeapMin
from pila import Stack

class Graph:
    def __init__(self, dirigido=False):
        self.elements = []  # corregido a 'elements' en lugar de 'elemnts'
        self.dirigido = dirigido
    
    def show_graph(self):
        print("\nNodos:")
        for index, nodo in enumerate(self.elements):
            print(nodo['value'])
            print("  Aristas:")
            for arista in nodo['aristas']:
                print(f"    Destino: {arista['value']} - Peso: {arista['peso']} metros")
        print()
    
    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index
        return None
    
    def insert_vertice(self, value):
        nodo = {
            'value': value,
            'aristas': [],
            'visitado': False,
        }
        self.elements.append(nodo)
    
    def search_arista(self, origen, destino):
        pos_origen = self.search(origen)
        if pos_origen is not None:
            for arista in self.elements[pos_origen]['aristas']:
                if arista['value'] == destino:
                    return arista
        return None


    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)  # corregido 'saerch' a 'search'
        if pos_origen is not None and pos_destino is not None:
            arista = {'value': destino, 'peso': peso}
            self.elements[pos_origen]['aristas'].append(arista)
            if not self.dirigido:
                arista = {'value': origen, 'peso': peso}
                self.elements[pos_destino]['aristas'].append(arista)
    
    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False
    
    def dijkstra(self, origen):
        from math import inf
        no_visitado = HeapMin()
        distancias = {nodo['value']: inf for nodo in self.elements}
        distancias[origen] = 0
        anteriores = {nodo['value']: None for nodo in self.elements}

        for nodo in self.elements:
            distancia = 0 if nodo['value'] == origen else inf
            no_visitado.arrive([nodo['value'], nodo, None], distancia)
        
        while len(no_visitado.elements) > 0:
            node = no_visitado.atention()
            costo_actual = node[0]
            nodo_actual = node[1][0]
            adyacentes = node[1][1]['aristas']
            for adyacente in adyacentes:
                nueva_distancia = costo_actual + adyacente['peso']
                if nueva_distancia < distancias[adyacente['value']]:
                    distancias[adyacente['value']] = nueva_distancia
                    anteriores[adyacente['value']] = nodo_actual
                    pos = no_visitado.search(adyacente['value'])
                    if pos is not None:
                        no_visitado.change_priority(pos, nueva_distancia)

        destino = 'sala de estar'
        camino = []
        while destino is not None: 
            camino.insert(0, destino)
            destino = anteriores[destino]
        return camino, distancias['sala de estar']
    
    def kruskal(self):
        def find(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index
            return None

        bosque = [[nodo['value']] for nodo in self.elements]
        aristas = HeapMin()
        for nodo in self.elements:
            for arista in nodo['aristas']:
                if self.search_arista(arista['value'], nodo['value']) is None:
                    aristas.arrive([nodo['value'], arista['value']], arista['peso'])
        
        arbol_expansion = []
        total_cable = 0

        while len(bosque) > 1 and len(aristas.elements) > 0:
            arista = aristas.atention()
            origen, destino = arista[1]
            pos_origen = find(bosque, origen)
            pos_destino = find(bosque, destino)

            if pos_origen != pos_destino:
                arbol_expansion.append((origen, destino, arista[0]))
                total_cable += arista[0]
                bosque[pos_origen].extend(bosque.pop(pos_destino))

        return arbol_expansion, total_cable

# Crear el grafo no dirigido
casa = Graph(dirigido=False)

# Insertar vértices (ambientes)
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", 
             "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]
for ambiente in ambientes:
    casa.insert_vertice(ambiente)

# Insertar aristas (con distancias en metros)
casa.insert_arista("cocina", "comedor", 5)
casa.insert_arista("cocina", "cochera", 10)
casa.insert_arista("cocina", "baño 1", 7)
casa.insert_arista("comedor", "sala de estar", 8)
casa.insert_arista("comedor", "patio", 12)
casa.insert_arista("comedor", "quincho", 15)
casa.insert_arista("habitación 1", "habitación 2", 6)
casa.insert_arista("habitación 1", "baño 2", 9)
casa.insert_arista("habitación 2", "sala de estar", 14)
casa.insert_arista("sala de estar", "terraza", 5)
casa.insert_arista("terraza", "patio", 10)
casa.insert_arista("quincho", "patio", 3)

# Mostrar el grafo
casa.show_graph()

# Obtener el árbol de expansión mínima
arbol_minimo, total_cable = casa.kruskal()
print("Árbol de expansión mínima:", arbol_minimo)
print("Total de cable necesario:", total_cable, "metros")

# Determinar el camino más corto desde la habitación 1 a la sala de estar
camino, distancia = casa.dijkstra("habitación 1")
print("Camino más corto desde habitación 1 a sala de estar:", camino)
print("Distancia total para cable de red:", distancia, "metros")
