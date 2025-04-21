from bigtree import Node, print_tree

# Crear nodos del árbol
gerentegeneral = Node("GERENTE GENERAL")                     # Nodo raíz
administrativo = Node("Dpto ADMINISTRATIVO", parent=gerentegeneral)
comercial = Node("Dpto COMERCIAL", parent=gerentegeneral) 
operaciones = Node("Dpto de OPERACIONES", parent=gerentegeneral) 

#DEPENDENCIAS DEL DEPARTAMENTO ADMINISTRATIVO
contabilidad = Node("CONTABILIDAD", parent=administrativo)
cartera = Node("CARTERA", parent=administrativo)
tesoreria = Node("TESORERIA", parent=administrativo) 
rh = Node("RECURSOS HUMANOS", parent=administrativo)

#DEPENDENCIAS DEL DEPARTAMENTO COMERCIAL
comprasnacionales = Node("COMPRAS NACIONALES", parent=comercial)
importaciones = Node("IMPORTACIONES", parent=comercial)
ventas = Node("VENTAS", parent=comercial)

#AREAS DE VENTAS
principal = Node("SEDE PRINCIPAL", parent=ventas)
sucursales = Node("SUCURSALES", parent=ventas)
web = Node("WEB SITE", parent=ventas)

#DEPENDENCIAS DEL DEPARTAMENTO DE OPERACIONES
bodegaje = Node("BODEGAJE", parent=operaciones)
reempaque = Node("REEMPAQUE", parent=operaciones)
despachos = Node("DESPACHOS", parent=operaciones)

# Mostrar el árbol
print("Imprime el árbol")
print_tree(gerentegeneral)

print("Imprime los nodos de forma descendiente lo que está abajo de GERENTE GENERAL")
for node in gerentegeneral.descendants:
    print(node.name)

print("Imprime los nodos hijos de Gerente General")
for node in gerentegeneral.children:
    print(node.name)

print("Imprime los nodos hijos de Ventas")
for node in ventas.children:
    print(node.name)

print("Verifica si la raiz es gerente general")
print(gerentegeneral.is_root)

print("Verifica si la raiz es el departamento administrativo")
print(administrativo.is_root)

print("Verifica si gerente general es una hoja")
print(gerentegeneral.is_leaf) 

#AGREGAR UN NODO HIJO A VENTAS
nuevo = Node("PROMOS")
nuevo.parent = ventas

#ELIMINAR EL NODO WEB
web.parent = None

print("Imprime el nuevo árbol")
print_tree(gerentegeneral)

