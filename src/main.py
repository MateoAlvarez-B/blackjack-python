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

def calcular_valor_mano(mano):
    """
    Calcula el valor total de una mano de Blackjack.
    El As vale 11, pero si el total supera 21, pasa a valer 1.
    """
    valor = 0      # Acumula el valor total de la mano
    ases = 0       # Cuenta cuántos Ases hay (porque pueden valer 11 o 1)

    for carta in mano:
        numero = carta[:-1]  # Extrae el valor de la carta (quita el palo)

        # Figuras valen 10
        if numero in ["J", "Q", "K"]:
            valor += 10

        # El As vale inicialmente 11
        elif numero == "A":
            valor += 11
            ases += 1        # Contamos el As para poder ajustarlo después

        # Cartas numéricas: convertir a entero
        else:
            valor += int(numero)

    # Ajustar el valor de los Ases si nos pasamos de 21
    while valor > 21 and ases > 0:
        valor -= 10   # Cambiar un As de 11 → 1 (restar 10 equivale a eso)
        ases -= 1     # Ya hemos ajustado un As

    return valor      # Devolver el valor final de la mano

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


