class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos 

class Node:
    def __init__(self, other_value):
        self.other_value = other_value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, value, other_value):
        if self.root is None:
            self.root = Node(other_value)
        else:
            self._insert(value, self.root, other_value)

    def _insert(self, value, current_node, other_value):
        if value < current_node.other_value.nombre:
            if current_node.left is None:
                current_node.left = Node(other_value)
            else:
                self._insert(value, current_node.left, other_value)
        elif value > current_node.other_value.nombre:
            if current_node.right is None:
                current_node.right = Node(other_value)
            else:
                self._insert(value, current_node.right, other_value)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        return None

    def _search(self, value, current_node):
        if value == current_node.other_value.nombre:
            return current_node
        elif value < current_node.other_value.nombre and current_node.left is not None:
            return self._search(value, current_node.left)
        elif value > current_node.other_value.nombre and current_node.right is not None:
            return self._search(value, current_node.right)
        return None


class PokemonBinaryTree(BinaryTree):
    def insert_node(self, pokemon):
        super().insert_node(pokemon.nombre, pokemon)

    def search_by_number(self, number):
        def __search_by_number(root, number):
            if root is not None:
                if root.other_value.numero == number:
                    return root
                elif number < root.other_value.numero:
                    return __search_by_number(root.left, number)
                else:
                    return __search_by_number(root.right, number)
            return None

        return __search_by_number(self.root, number)

    def proximity_search(self, search_value):
        def __proximity_search(root, search_value):
            if root is not None:
                __proximity_search(root.left, search_value)
                if root.other_value.nombre.startswith(search_value):
                    print(root.other_value.nombre)
                __proximity_search(root.right, search_value)

        if self.root is not None:
            __proximity_search(self.root, search_value)

    def list_by_type(self, tipo):
        def __list_by_type(root, tipo):
            if root is not None:
                __list_by_type(root.left, tipo)
                if tipo in root.other_value.tipos:
                    print(root.other_value.nombre)
                __list_by_type(root.right, tipo)

        if self.root is not None:
            __list_by_type(self.root, tipo)

    def inorden_numero(self):
        def __inorden_numero(root):
            if root is not None:
                __inorden_numero(root.left)
                print(f"{root.other_value.numero}: {root.other_value.nombre}")
                __inorden_numero(root.right)

        if self.root is not None:
            __inorden_numero(self.root)

    def inorden_nombre(self):
        def __inorden_nombre(root):
            if root is not None:
                __inorden_nombre(root.left)
                print(root.other_value.nombre)
                __inorden_nombre(root.right)

        if self.root is not None:
            __inorden_nombre(self.root)


# Inicializo los árboles
arbol_pokemons_por_nombre = PokemonBinaryTree()
arbol_pokemons_por_numero = PokemonBinaryTree()
arbol_pokemons_por_tipo = PokemonBinaryTree()

# Lista inventada
pokemons = [
    Pokemon("Bulbasaur", 1, ["Planta", "Veneno"]),
    Pokemon("Charmander", 2, ["Fuego"]),
    Pokemon("Squirtle", 3, ["Agua"]),
    Pokemon("Pikachu", 4, ["Eléctrico"]),
    Pokemon("Gengar", 5, ["Fantasma", "Veneno"]),
    Pokemon("Charizard", 6, ["Fuego", "Volador"]),
    Pokemon("Lucario", 7, ["Lucha", "Acero"]),
    Pokemon("Eevee", 8, ["Normal"]),
    Pokemon("Jolteon", 9, ["Eléctrico"]),
    Pokemon("Lycanroc", 10, ["Roca"]),
    Pokemon("Tyrantrum", 11, ["Roca", "Dragón"]),
]


for pokemon in pokemons:
    arbol_pokemons_por_nombre.insert_node(pokemon)
    arbol_pokemons_por_numero.insert_node(pokemon)
    for tipo in pokemon.tipos:
        arbol_pokemons_por_tipo.insert_node(pokemon)

# a) Mostrar todos los datos de un Pokemon a partir de su numero y nombre
def mostrar_datos_pokemon(nombre, numero):
    pokemon_by_name = arbol_pokemons_por_nombre.search(nombre)
    pokemon_by_number = arbol_pokemons_por_numero.search_by_number(numero)
    if pokemon_by_name:
        print(f"Datos de {pokemon_by_name.other_value.nombre}: {pokemon_by_name.other_value.tipos}")
    if pokemon_by_number:
        print(f"Datos de {pokemon_by_number.other_value.nombre}: {pokemon_by_number.other_value.tipos}")

# b) Mostrar nombres de Pokémon de un tipo específico
def mostrar_pokemons_por_tipo(tipo):
    print(f"Pokémon de tipo {tipo}:")
    arbol_pokemons_por_tipo.list_by_type(tipo)

# c) Listado en orden ascendente por numero
def listado_por_numero():
    print("Listado de Pokémon por número:")
    arbol_pokemons_por_numero.inorden_numero()

# d) Listado por nombre
def listado_por_nombre():
    print("Listado de Pokémon por nombre:")
    arbol_pokemons_por_nombre.inorden_nombre()

# e) Mostrar datos específicos de ciertos Pokemon
def mostrar_datos_especificos():
    nombres_especificos = ["Jolteon", "Lycanroc", "Tyrantrum"]
    print("Datos específicos de Pokémon:")
    for nombre in nombres_especificos:
        pokemon = arbol_pokemons_por_nombre.search(nombre)
        if pokemon:
            print(f"Datos de {pokemon.other_value.nombre}: {pokemon.other_value.tipos}")

# f) Contar Pokemon de tipos específicos
def contar_pokemons_por_tipo(tipo):
    count = 0
    def __contar(root):
        nonlocal count
        if root is not None:
            if tipo in root.other_value.tipos:
                count += 1
            __contar(root.left)
            __contar(root.right)

    __contar(arbol_pokemons_por_tipo.root)
    return count

def buscar_por_proximidad(search_value):
    print(f"Buscando Pokémon cuyos nombres comienzan con '{search_value}':")
    arbol_pokemons_por_nombre.proximity_search(search_value)



# Implementacion
buscar_por_proximidad('Bul')
mostrar_datos_pokemon("Bulbasaur", 1)
mostrar_datos_pokemon("Pikachu", 4)
mostrar_pokemons_por_tipo("Fuego")
listado_por_numero()
listado_por_nombre()
mostrar_datos_especificos()
print("Cantidad de Pokémon de tipo Eléctrico:", contar_pokemons_por_tipo("Eléctrico"))
print("Cantidad de Pokémon de tipo Acero:", contar_pokemons_por_tipo("Acero"))
