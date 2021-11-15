from random import randint, seed
from functools import reduce

class Objeto:
    def __init__(self, go: int, po: int, i: int) -> None:
        self.go = go
        self.po = po
        self.id = i

    def __repr__(self) -> str:
        return f'{self.id} {self.go} {self.po}'

def Miope(objetos: list, cmax: int, inicial = ..., alfa: int = 1) -> list:
    solucion, peso = ([inicial], inicial.po) if inicial != ... else ([], 0)

    objetosOrdenados = sorted(objetos, key=lambda o: o.go/o.po)
    while objetosOrdenados and peso < cmax:
        # Saco de la lista un objeto al azar dentro de los <alfa> últimos.
        objeto = objetosOrdenados.pop(-randint(1, min(alfa, len(objetosOrdenados))))
        # Si cabe en la mochila lo agrego.
        if peso + objeto.po <= cmax:
            solucion.append(objeto)
            peso += objeto.po
    return solucion

def Greedy(archivo: str, puntoDePartida: int = ..., alfa: int = 1) -> list:
    with open(archivo, 'r') as puntero:
        objetos = []
        _, cmax = map(int, puntero.readline().strip().split(' '))
        i = 0
        for linea in puntero:
            objetos.append(Objeto(*map(int, linea.strip().split(' ')), i))
            i += 1
    solucion = Miope(objetos, cmax, ... if puntoDePartida == ... else objetos.pop(puntoDePartida), alfa)
    print(reduce(lambda a, o: a + o.go, solucion, 0), reduce(lambda a, o: a + o.po, solucion, 0))
    return solucion

def GreedyAleatorizado(archivo: str, alfa: int = 1) -> list:
    with open(archivo, 'r') as puntero:
        count = sum(1 for _ in puntero)
    print(f'Punto de partida: {(puntoDePartida := randint(0, count - 2))}')
    return Greedy(archivo, puntoDePartida, alfa)

def main():
    seed(269)
    print(Greedy('f1_l-d_kp_10_269.txt', alfa=3))
    print(GreedyAleatorizado('f1_l-d_kp_10_269.txt', alfa=3))

if __name__ == '__main__':
    main()
