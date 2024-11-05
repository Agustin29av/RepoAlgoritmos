
from cola import Queue

class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None, capturada=None, descripcion=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.capturada = capturada
            self.height = 0
            self.descripcion = descripcion
            
            

    def __init__(self):
        self.root = None

    def height(self, root): #altura
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root): #altura_actualización
        if root is not None:    
            # print(f'actualizar altura de {root.value}')
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1
            # print(f'altura izq {left_height} altura der {right_height}')
            # print(f'altura de {root.value} es {root.height}')

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux) 
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root): 
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                # print('desbalanceado a la izquierda')
                if self.height(root.left.left) >= self.height(root.left.right):
                    # print('rotar simple derecha')
                    root = self.simple_rotation(root, True)
                else:
                    # print('rotar doble derecha')
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                # print('desbalanceado a la derecha')
                if self.height(root.right.right) >= self.height(root.right.left):
                    # print('rotar simple izquierda')
                    root = self.simple_rotation(root, False)
                else:
                    # print('rotar doble izquierda')
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None, capturada=None):
        def __insert(root, value, other_value=None, capturada=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value, capturada=capturada)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value, capturada)
            else:
                root.right = __insert(root.right, value, other_value, capturada)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_value, capturada)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    # print('lo encontre')
                    return root
                elif key < root.value:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, key)
            else:
                print('no hay nada')
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                # print(f'izquierda de {root.value}')
                __preorden(root.left)
                # print(f'derecha de {root.value}')
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)
    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)
    def proximity_search(self, search_value):
        def __proximity_search(root, search_value):
            if root is not None:
                __proximity_search(root.left, search_value)
                if root.value.startswith(search_value):
                    print(root.value)
                __proximity_search(root.right, search_value)

        if self.root is not None:
            __proximity_search(self.root, search_value)

    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(f"nivel {node.height}", node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplaz+ar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            extra_data_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete, extra_data_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete, extra_data_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    extra_data_delete = root.other_value
                    if root.left is None:
                        # print('a la izquierda no hay nada')
                        return root.right, value_delete, extra_data_delete 
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete, extra_data_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_value = replace_node.other_value
                        # return root, value_delete
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value_delete, extra_data_delete

        delete_value = None
        delete_extra_value = None
        if self.root is not None:
            self.root, delete_value, delete_extra_value = __delete(self.root, value)
        return delete_value, delete_extra_value
    
    
    def contar_super_heroes(self):
        def __contar_super_heroes(root):
            counter = 0
            if root is not None:
                if root.other_value.get('is_hero') is True:
                    counter = 1
                counter += __contar_super_heroes(root.left)
                counter += __contar_super_heroes(root.right)
            return counter

        return __contar_super_heroes(self.root)
    
    def contar_villanos(self):
        def __contar_villanos(root):
            counter = 0
            if root is not None:
                if root.other_value.get('is_hero') is not True:
                    counter = 1
                counter += __contar_villanos(root.left)
                counter += __contar_villanos(root.right)
            return counter

        return __contar_villanos(self.root)
    
    def inorden_con_derrotas(self):
        def __inorden_con_derrotas(root):
            if root is not None:
                __inorden_con_derrotas(root.left)
                derrotado = root.other_value.get("derrotado","Nadie")
                if derrotado is None:
                    derrotado="Nadie"
                print(f'{root.value}: derrotado por {derrotado}')
                __inorden_con_derrotas(root.right)
        if self.root is not None:
            __inorden_con_derrotas(self.root)
    
    def modificarCapturas(self, criatura, capturador):
        nodo = self.search(criatura)
        if nodo is not None:
            nodo.capturada = capturador
            print(f'{criatura} ha sido capturada por {capturador}.')

    def eliminarCriaturas(self, nombre):
        self.delete_node(nombre)
        print(f"Personaje '{nombre}' eliminado")
    
    def modificar_nombre(self, nombre_viejo, nombre_nuevo):
        nodo = self.search(nombre_viejo)
        if nodo:
            nodo.value = nombre_nuevo
            print(f'{nombre_viejo} ha sido renombrado a {nombre_nuevo}.')

    def criaturas_capturadas_por_in(self, capturador): #INORDEN
        def __capturadas(root, capturador):
            if root is not None:
                __capturadas(root.left, capturador)
                if root.capturada == capturador:
                    print(f"{root.value} fue capturada por {capturador}.")
                __capturadas(root.right, capturador)
        if self.root is not None:
            __capturadas(self.root, capturador)

    def criaturas_capturadas_por_pre(self, capturador): #PREORDEN
        def __capturadas(root, capturador):
            if root is not None:
                if root.capturada == capturador:
                    print(f"{root.value} fue capturada por {capturador}.")
                __capturadas(root.left, capturador)
                __capturadas(root.right, capturador)
        if self.root is not None:
            __capturadas(self.root, capturador)
   

    def modificarCapturas(self, criatura, capturador):
        nodo = self.search(criatura)
        if nodo is not None:
            nodo.capturada = capturador
            print(f'{criatura} Se actualizo, su captaurador es:  {capturador}.') 



    def cargar_descripcion(self, criatura, descripcion):
        nodo = self.search(criatura)
        if nodo is not None:
            nodo.descripcion = descripcion
            print(f'Descripcion de {criatura} actualizada: {descripcion}')
        else: 
            print(f'Criatura {criatura} no encontrada en el arbol')

    def mostrar_info(self, criatura):
        nodo = self.search(criatura)
        if nodo:
            print(f"Criatura: {nodo.value}")
            print(f"Descripción: {nodo.descripcion}")
            print(f"Derrotado por: {nodo.other_value.get('derrotado', 'Nadie')}")
            print(f"Capturado por: {nodo.capturada}")
        else:
            print(f"{criatura} no encontrada.")
    
    #top 3 de los que mas cantidad de criaturas mataron

    def top_heroes(self):
        derrotadores = {}
        def __contar_derrotadores(root):
            if root is not None:
                derrotador = root.other_value.get("derrotado", None)
                if derrotador:
                    if derrotador in derrotadores:
                        derrotadores[derrotador]+=1
                    else:
                        derrotadores[derrotador]=1
                __contar_derrotadores(root.left)
                __contar_derrotadores(root.right)
        __contar_derrotadores(self.root)
        top_3=sorted(derrotadores.items(),key=lambda x: x[1], reverse=True)[:3]
        for heroe, cantidad in top_3:
            print(f'{heroe}: {cantidad} criaturas derrotadas')    

    # Criaturas derrotadas por Heracles

    def criaturas_derrotadas_por(self, heroe):
        def __derrotadas(root, heroe):
            if root is not None:
                if root.other_value.get("derrotado") == heroe:
                    print(f'{root.value} fue derrotado por {heroe}')
                __derrotadas(root.left, heroe)
                __derrotadas(root.right, heroe)
        if self.root is not None:
            __derrotadas(self.root, heroe)
    
    # Criaturas que no han sido derrotadas

    def criaturas_sin_derrotar(self):
        def __sinDerrota(root):
            if root is not None:
                if root.other_value.get("derrotado") is None:
                    print(f'{root.value} no ha sido derrotado')
                __sinDerrota(root.left)
                __sinDerrota(root.right)
        if self.root is not None:
            __sinDerrota(self.root)
    
    def modificarCapturas(self, criatura, capturador):
        nodo = self.search(criatura)
        if nodo is not None:
            nodo.capturada = capturador
            print(f'{criatura} Se actualizo, su captaurador es:  {capturador}.') 
    
    def modificarCriatura(self, nombre, nuevo_valor):
        nodo = self.search(nombre)
        if nodo:
            nodo.descripcion = nuevo_valor
            print(f'Personaje {nombre} modificado a: {nuevo_valor}')
        else:
            print(f'Personaje {nombre} no encontrado')

    def por_nivel_perso(self): #PREGUNTAR SI ESTA BIEN
        pendientes = Queue()  # Usamos tu implementación de la cola
        if self.root is not None:
            pendientes.arrive((self.root, 0))  # Encolamos la raíz y el nivel 0

        while pendientes.size() > 0:
            node, nivel = pendientes.attention()  # Desencolamos el nodo y su nivel
            print(f"Nivel {nivel}: {node.value}")  # Imprimimos el valor con su nivel
            
            # Encolamos los hijos con su nivel correspondiente
            if node.left is not None:
                pendientes.arrive((node.left, nivel + 1))
            if node.right is not None:
                pendientes.arrive((node.right, nivel + 1))
    


    