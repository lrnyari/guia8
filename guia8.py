from queue import LifoQueue as Pila
import random

def copiar_pila(p: Pila) -> Pila:
    paux = Pila()
    res = Pila()
    
    while(not p.empty()):
        elem = p.get()
        paux.put(elem)
    
    while(not paux.empty()):
        elem = paux.get()
        p.put(elem)
        res.put(elem)

    return res


def contar_elementos_pila(p: Pila) -> int:
    cantidad:int = 0
    paux = copiar_pila(p)

    while(not paux.empty()):
        elem = paux.get()
        cantidad += 1
    
    return cantidad

#ESTÀ MAL ROMPE CANTIDAD
#def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila:
#    p = Pila()
#    while(cantidad > 0):
#        p.put(random.randint(desde,hasta))
#        cantidad -= 1
#    
#    return p

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila:
    pila_res = Pila()

    for _ in range(cantidad):
        valor:int = random.randint(desde, hasta)
        pila_res.put(valor)
    
    return pila_res

def buscar_el_maximo(p: Pila[int]) -> int:
    paux = copiar_pila(p)
    maximo:int = 0
    aux:int = 0

    while(not paux.empty()):
        aux = paux.get()

        if(aux > maximo):
            maximo = aux

    return maximo
        



mi_pila = Pila()
mi_pila.put(2)
mi_pila.put(8)
mi_pila.put(9)

print(contar_elementos_pila(mi_pila))
print(contar_elementos_pila(mi_pila))

#print(list(generar_nros_al_azar(4,0,9).queue))
print(generar_nros_al_azar(4,0,9).queue)
print(buscar_el_maximo(mi_pila))

#ARCHIVOS
import typing
def contar_lineas(nombre_archivo: str) -> int:
    #para tipar el archivo necesito importar modulo typing
    arch:typing.IO = open(nombre_archivo, "r")
    lineas:[str] = arch.readlines()
    arch.close()
    return len(lineas)

print(contar_lineas("archivo_prueba.txt"))

def es_comentario(linea: str) -> bool:
    i: int = 0
    #salteo todos los espacios al principio
    while(i < len(linea) and linea[i] == " "):
        i += 1
    return i < len(linea) and linea[i] == "#"

def clonar_sin_comentarios(nombre_archivo: str):
    arch = open(nombre_archivo, "r")
    res = open("resultado.txt", "w")

    lineas:[str] = arch.readlines()

    for linea in lineas:
        if(not es_comentario(linea)):
            res.write(linea)
    
    arch.close()
    res.close()

clonar_sin_comentarios("archivo_prueba.txt")
