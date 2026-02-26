# Importamos el módulo random para poder mezclar la baraja
import random

# Lista con los palos de la baraja
# ♠ = picas, ♥ = corazones, ♦ = diamantes, ♣ = tréboles
PALOS = ["♠", "♥", "♦", "♣"]

# Lista con los valores posibles de las cartas
# A = As, J = Jack (Sota), Q = Queen (Reina), K = King (Rey)
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def crear_baraja():
    palos = ["♠", "♥", "♦", "♣"]
    numeros = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

    baraja = [numero + palo for palo in palos for numero in numeros]
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

def repartir_manos_iniciales(baraja):
    """
    Reparte dos cartas al jugador y dos al dealer.
    Devuelve:
    - mano_jugador
    - mano_dealer
    - baraja_restante
    """
    mano_jugador = []
    mano_dealer = []

    for _ in range(2):
        carta, baraja = repartir_carta(baraja)
        mano_jugador.append(carta)

        carta, baraja = repartir_carta(baraja)
        mano_dealer.append(carta)

    return mano_jugador, mano_dealer, baraja

def mostrar_mano(nombre, mano):
    valor = calcular_valor_mano(mano)
    cartas = ", ".join(mano)
    print(f"{nombre}: {cartas}  (valor: {valor})")

def turno_jugador(mano_jugador, baraja):
    while True:
        mostrar_mano("Jugador", mano_jugador)

        decision = input("¿Quieres pedir carta (p) o plantarte (s)? ").lower()

        if decision == "s":
            break

        if decision == "p":
            carta, baraja = repartir_carta(baraja)
            mano_jugador.append(carta)

            if calcular_valor_mano(mano_jugador) > 21:
                mostrar_mano("Jugador", mano_jugador)
                print("Te has pasado de 21. Pierdes.")
                break

    return mano_jugador, baraja

def turno_dealer(mano_dealer, baraja):
    print("\nTurno del dealer...")

    while calcular_valor_mano(mano_dealer) < 17:
        carta, baraja = repartir_carta(baraja)
        mano_dealer.append(carta)
        print(f"El dealer pide carta: {carta}")

    mostrar_mano("Dealer", mano_dealer)

    if calcular_valor_mano(mano_dealer) > 21:
        print("El dealer se ha pasado de 21.")
    
    return mano_dealer, baraja

def determinar_ganador(mano_jugador, mano_dealer):
    valor_jugador = calcular_valor_mano(mano_jugador)
    valor_dealer = calcular_valor_mano(mano_dealer)

    if valor_jugador > 21:
        return "Dealer"
    if valor_dealer > 21:
        return "Jugador"

    if valor_jugador > valor_dealer:
        return "Jugador"
    elif valor_dealer > valor_jugador:
        return "Dealer"
    else:
        return "Empate"

def jugar_partida():
    print("=== Bienvenido al Blackjack ===")

    # Crear baraja
    baraja = crear_baraja()

    # Repartir manos iniciales
    mano_jugador, mano_dealer, baraja = repartir_manos_iniciales(baraja)

    print("\nTus cartas iniciales:")
    mostrar_mano("Jugador", mano_jugador)

    print("\nCarta visible del dealer:")
    print(f"Dealer: {mano_dealer[0]}, ?")

    # Turno del jugador
    mano_jugador, baraja = turno_jugador(mano_jugador, baraja)

    # Si el jugador se pasa, termina la partida
    if calcular_valor_mano(mano_jugador) > 21:
        print("\nEl dealer gana.")
        return

    # Turno del dealer
    mano_dealer, baraja = turno_dealer(mano_dealer, baraja)

    # Determinar ganador
    ganador = determinar_ganador(mano_jugador, mano_dealer)

    print("\n=== Resultado final ===")
    mostrar_mano("Jugador", mano_jugador)
    mostrar_mano("Dealer", mano_dealer)

    if ganador == "Jugador":
        print("\n¡Has ganado!")
    elif ganador == "Dealer":
        print("\nEl dealer gana.")
    else:
        print("\nEmpate.")
if __name__ == "__main__":
    jugar_partida()

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







