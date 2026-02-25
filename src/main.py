# Importamos el módulo random para poder mezclar la baraja
import random

# Lista con los palos de la baraja
# ♠ = picas, ♥ = corazones, ♦ = diamantes, ♣ = tréboles
PALOS = ["♠", "♥", "♦", "♣"]

# Lista con los valores posibles de las cartas
# A = As, J = Jack (Sota), Q = Queen (Reina), K = King (Rey)
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def crear_baraja():
    """
    Crea una baraja estándar de 52 cartas.
    Cada carta es una tupla (valor, palo).
    """

    # Creamos una lista de cartas usando comprensión de listas
    # Recorre cada palo y para cada palo recorre todos los valores
    # Genera combinaciones como: ("A", "♠"), ("2", "♠"), etc.
    baraja = [(valor, palo) for palo in PALOS for valor in VALORES]

    # Mezclamos la lista de cartas de forma aleatoria
    # shuffle modifica la lista original (no devuelve una nueva)
    random.shuffle(baraja)

    # Devolvemos la baraja ya creada y mezclada
    return baraja

def repartir_carta(baraja):
    """
    Saca la primera carta de la baraja y devuelve:
    - la carta extraída
    - la baraja restante
    """
    # pop(0) elimina y devuelve el elemento que está en la posición 0 de la lista, 
    # es decir, el primer elemento.
    carta = baraja.pop(0)
    return carta, baraja


# Este bloque solo se ejecuta si el archivo se ejecuta directamente
# (no si se importa como módulo en otro archivo)
if __name__ == "__main__":

    # Llamamos a la función para crear la baraja
    baraja = crear_baraja()

    # Mostramos cuántas cartas tiene la baraja
    # len() devuelve el número de elementos de la lista
    print(f"Baraja creada con {len(baraja)} cartas")

    # Mostramos solo las primeras 5 cartas
    # baraja[:5] significa "desde la posición 0 hasta la 4"
    print(baraja[:5])

