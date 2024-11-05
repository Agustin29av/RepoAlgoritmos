from arbol_avl import BinaryTree

criaturas = [
    {
        "nombre": "Ceto",
        "derrotado": None
    },
    {
        "nombre": "Tifon",
        "derrotado": "Zeuz"
    },
    {
        "nombre": "Equidna",
        "derrotado": "Argos Panoptes"
    },
    {
        "nombre": "Dino",
        "derrotado": None
    },
    {
        "nombre": "Pefredo",
        "derrotado": None
    },
    {
        "nombre": "Enio",
        "derrotado": None
    },
    {
        "nombre": "Escila",
        "derrotado": None
    },
    {
        "nombre": "Caribdis",
        "derrotado": None
    },
    {
        "nombre": "Euriale",
        "derrotado": None
    },
    {
        "nombre": "Esteno",
        "derrotado": None
    },
    {
        "nombre": "Medusa",
        "derrotado": "Perseo"
    },
    {
        "nombre": "Ladon",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Aguila del Caucaso",
        "derrotado": None
    },
    {
        "nombre": "Quimera",
        "derrotado": "Belerofonte"
    },
    {
        "nombre": "Hidra de Lerna",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Leon de Nemea",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Esfinge",
        "derrotado": "Edipo"
    },
    {
        "nombre": "Dragon de la Colquida",
        "derrotado": None
    },
    {
        "nombre": "Cerbero",
        "derrotado": None
    },
    {
        "nombre": "Cerdo de Cromion",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Ortro",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Toro de Creta",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Jabali de Calidon",
        "derrotado": "Atalanta"
    },
    {
        "nombre": "Carcinos",
        "derrotado": None
    },
    {
        "nombre": "Gerion",
        "derrotado": "Heracles"
    },
    {
        "nombre": "Cloto",
        "derrotado": None
    },
    {
        "nombre": "Laquesis",
        "derrotado": None
    },
    {
        "nombre": "Artropos",
        "derrotado": None
    },
    {
        "nombre": "Minotauro de Creta",
        "derrotado": "Teseo"
    },
    {
        "nombre": "Harpias",
        "derrotado": None
    },
    {
        "nombre": "Argos Panoptes",
        "derrotado": "Hermes"
    },
    {
        "nombre": "Aves de Estinfalo",
        "derrotado": None
    },
    {
        "nombre": "Talos",
        "derrotado": "Medea"
    },
    {
        "nombre": "Sirenas",
        "derrotado": None
    },
    {
        "nombre": "Piton",
        "derrotado": "Apolo"
    },
    {
        "nombre": "Cierva de Cerinea",
        "derrotado": None
    },
    {
        "nombre": "Basilisco",
        "derrotado": None
    },
    {
        "nombre": "Jabali de Erimanto",
        "derrotado": None
    }
]

arbol = BinaryTree()

for criatura in criaturas:
    arbol.insert_node(criatura["nombre"], {"derrotado": criatura["derrotado"]})
    #print(f'{criatura["nombre"]} se inerto correctamente')

# a)
#arbol.inorden_con_derrotas()

# b)
#arbol.cargar_descripcion("Ceto", "Una criatura mitologica de los mares")
#arbol.cargar_descripcion("Medusa", "Una de las gorgonas, derrotada por Perseo")

# c)
#print("\nMostrar Informacion de Talos")
#nodo_talos=arbol.search("Talos")
#if nodo_talos:
#    print(f'Talos fue derrotado por {nodo_talos.other_value.get('derrotado','Nadie')}')

# d)
#arbol.top_heroes()

# e)
#arbol.criaturas_derrotadas_por("Heracles")

# f)
#arbol.criaturas_sin_derrotar()

#punto g) y h)
arbol.modificarCapturas('Cerbero', 'Heracles')
arbol.modificarCapturas('Toro de Creta', 'Heracles')
arbol.modificarCapturas('Cierva de Cerinea', 'Heracles')
arbol.modificarCapturas('Jabali de Erimanto', 'Heracles')

#punto i)
#arbol.proximity_search('Ce')

#punto j)
#arbol.eliminarCriaturas('Basilisco')
#arbol.eliminarCriaturas('Sirenas')

#punto k)
#arbol.modificarCriatura('Aves de Estinfalo','Heracles derroto a varias Aves del Estinfalo')

#punto l)
#arbol.modificar_nombre('Ladon', 'Dragon Ladon')
#arbol.inorden()

#punto m)
arbol.by_level()
arbol.por_nivel_perso()

#punto n)
arbol.criaturas_capturadas_por_in("Heracles")
#arbol.criaturas_capturadas_por_preorden("Heracles")    


