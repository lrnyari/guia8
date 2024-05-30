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

def buscar_el_maximo(p: Pila) -> int:
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