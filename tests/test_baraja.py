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

def test_prueba():
    assert True

