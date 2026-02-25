# Importamos la función crear_baraja desde el archivo src/main.py
# Esto nos permite usar la función en este archivo de tests
from src.main import crear_baraja, repartir_carta

# Definimos una función de test
# El nombre empieza por "test_" porque frameworks como pytest
# detectan automáticamente funciones que empiecen así
def test_baraja_tiene_52_cartas():

    # Creamos una baraja llamando a la función que queremos probar
    baraja = crear_baraja()

    # Comprobamos que la baraja tenga exactamente 52 cartas
    # len(baraja) devuelve el número de elementos de la lista
    # Si no es 52, el test falla automáticamente
    assert len(baraja) == 52

# Segundo test
def test_baraja_no_tiene_duplicados():

    # Creamos otra baraja
    baraja = crear_baraja()

    # Convertimos la lista en un set
    # Un set NO permite elementos duplicados
    # Si hubiera cartas repetidas, el tamaño disminuiría
    assert len(baraja) == len(set(baraja))

def test_repartir_carta_devuelve_una_carta():
    baraja = crear_baraja()
    carta, baraja_restante = repartir_carta(baraja)

    assert carta is not None
    assert len(baraja_restante) == 51

def test_repartir_carta_quita_la_carta_de_la_baraja():
    baraja = crear_baraja()
    carta1, baraja = repartir_carta(baraja)
    carta2, baraja = repartir_carta(baraja)

    assert carta1 != carta2
    assert len(baraja) == 50

from src.main import calcular_valor_mano

def test_valor_sin_ases():
    # Mano sin Ases: solo se suman valores directos
    mano = ["10♣", "9♦"]
    assert calcular_valor_mano(mano) == 19

def test_valor_con_un_as_sin_pasarse():
    # Un As que puede valer 11 sin superar 21
    mano = ["A♠", "8♦"]
    assert calcular_valor_mano(mano) == 19

def test_valor_con_un_as_pasandose():
    # Un As que inicialmente vale 11, pero debe ajustarse a 1
    mano = ["A♠", "9♦", "5♥"]
    assert calcular_valor_mano(mano) == 15  # 11 + 9 + 5 = 25 → ajustar As → 15

def test_valor_con_dos_ases():
    # Dos Ases: uno vale 11 y el otro se ajusta a 1
    mano = ["A♠", "A♥"]
    assert calcular_valor_mano(mano) == 12  # 11 + 1

def test_valor_blackjack():
    # Blackjack natural: As + figura = 21
    mano = ["A♠", "K♦"]
    assert calcular_valor_mano(mano) == 21
from src.main import repartir_manos_iniciales

def test_repartir_manos_iniciales():
    baraja = crear_baraja()
    mano_jugador, mano_dealer, baraja_restante = repartir_manos_iniciales(baraja)

    assert len(mano_jugador) == 2
    assert len(mano_dealer) == 2
    assert len(baraja_restante) == 52 - 4
    assert mano_jugador[0] != mano_dealer[0]  # No deben ser la misma carta

def test_prueba():
    assert True

