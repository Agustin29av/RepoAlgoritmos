class Wonder:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo  # 'natural' o 'arquitectónica'
        self.distancias = []  # Lista de distancias a otras maravillas

class Grafo:
    def __init__(self):
        self.maravillas = []

    def agregar_maravilla(self, nombre, pais, tipo):
        nueva_maravilla = Wonder(nombre, pais, tipo)
        self.maravillas.append(nueva_maravilla)

    def agregar_distancia(self, origen, destino, distancia):
        idx_origen = self.buscar(origen)
        idx_destino = self.buscar(destino)
        if idx_origen is not None and idx_destino is not None:
            self.maravillas[idx_origen].distancias.append((self.maravillas[idx_destino], distancia))
            self.maravillas[idx_destino].distancias.append((self.maravillas[idx_origen], distancia))  # Grafo no dirigido

    def buscar(self, nombre):
        for i, maravilla in enumerate(self.maravillas):
            if maravilla.nombre == nombre:
                return i
        return None

    def mostrar_grafo(self):
        for maravilla in self.maravillas:
            print(f"{maravilla.nombre} ({maravilla.tipo}, {maravilla.pais})")
            for destino, peso in maravilla.distancias:
                print(f"    -> {destino.nombre} distancia: {peso}")

    def kruskal(self):
        aristas = []
        for maravilla in self.maravillas:
            for destino, peso in maravilla.distancias:
                if (destino.nombre, maravilla.nombre, peso) not in aristas:  # Evitar duplicados
                    aristas.append((maravilla.nombre, destino.nombre, peso))

        aristas.sort(key=lambda x: x[2])  # Ordenar por distancia
        bosque = {maravilla.nombre: maravilla.nombre for maravilla in self.maravillas}  # Cada maravilla es su propio líder

        def encontrar(v):
            if bosque[v] != v:
                bosque[v] = encontrar(bosque[v])
            return bosque[v]

        def unir(v1, v2):
            raiz1 = encontrar(v1)
            raiz2 = encontrar(v2)
            if raiz1 != raiz2:
                bosque[raiz2] = raiz1  # Unir el conjunto

        arbol_expansion = []
        for origen, destino, peso in aristas:
            if encontrar(origen) != encontrar(destino):
                unir(origen, destino)
                arbol_expansion.append((origen, destino, peso))

        return arbol_expansion

    def paises_con_maravillas(self):
        paises_architectonicos = set()
        paises_naturales = set()
        for maravilla in self.maravillas:
            if maravilla.tipo == 'arquitectónica':
                paises_architectonicos.add(maravilla.pais)
            else:
                paises_naturales.add(maravilla.pais)
        return paises_architectonicos, paises_naturales

    def paises_con_variadas_maravillas(self):
        conteo_paises = {}
        for maravilla in self.maravillas:
            if maravilla.pais in conteo_paises:
                conteo_paises[maravilla.pais] += 1
            else:
                conteo_paises[maravilla.pais] = 1
        return {pais: count for pais, count in conteo_paises.items() if count > 1}

# Creación del grafo
grafo = Grafo()

# Agregar maravillas
maravillas = [
    ('Chichen Itza', 'México', 'arquitectónica'),
    ('Cristo Redentor', 'Brasil', 'arquitectónica'),
    ('Machu Picchu', 'Perú', 'arquitectónica'),
    ('Colosseum', 'Italia', 'arquitectónica'),
    ('Taj Mahal', 'India', 'arquitectónica'),
    ('Great Wall of China', 'China', 'arquitectónica'),
    ('Petra', 'Jordania', 'arquitectónica'),
    ('Amazon Rainforest', 'Brasil', 'natural'),
    ('Halong Bay', 'Vietnam', 'natural'),
    ('Iguazu Falls', 'Argentina/Brasil', 'natural'),
    ('Komodo Island', 'Indonesia', 'natural'),
    ('Puerto Princesa Underground River', 'Filipinas', 'natural'),
    ('Table Mountain', 'Sudáfrica', 'natural'),
    ('Giants Causeway', 'Irlanda del Norte', 'natural'),
]

for nombre, pais, tipo in maravillas:
    grafo.agregar_maravilla(nombre, pais, tipo)

# Agregar distancias
grafo.agregar_distancia('Chichen Itza', 'Cristo Redentor', 4500)
grafo.agregar_distancia('Chichen Itza', 'Machu Picchu', 4000)
grafo.agregar_distancia('Machu Picchu', 'Colosseum', 10000)
grafo.agregar_distancia('Colosseum', 'Taj Mahal', 6200)
grafo.agregar_distancia('Taj Mahal', 'Great Wall of China', 3500)
grafo.agregar_distancia('Great Wall of China', 'Petra', 7000)
grafo.agregar_distancia('Cristo Redentor', 'Iguazu Falls', 1400)
grafo.agregar_distancia('Amazon Rainforest', 'Halong Bay', 8000)
grafo.agregar_distancia('Halong Bay', 'Komodo Island', 4000)
grafo.agregar_distancia('Komodo Island', 'Puerto Princesa Underground River', 3000)
grafo.agregar_distancia('Table Mountain', 'Giants Causeway', 6000)

# Mostrar el grafo
grafo.mostrar_grafo()

# Hallar el árbol de expansión mínimo
arbol_expansion = grafo.kruskal()
print("Árbol de expansión mínimo:")
for origen, destino, peso in arbol_expansion:
    print(f"{origen} - {destino} con peso: {peso}")

# Determinar países que tienen maravillas arquitectónicas y naturales
paises_architectonicos, paises_naturales = grafo.paises_con_maravillas()
print("Países con maravillas arquitectónicas:", paises_architectonicos)
print("Países con maravillas naturales:", paises_naturales)

# Determinar si hay países con más de una maravilla del mismo tipo
multiple_wonders = grafo.paises_con_variadas_maravillas()
print("Países con más de una maravilla del mismo tipo:", multiple_wonders)
