from functools import reduce

class Objeto:
    cantidad = 0

    def __init__(self, go: int, po: int) -> None:
        self.go = go
        self.po = po
        self.id = Objeto.cantidad
        Objeto.cantidad += 1

    def __repr__(self) -> str:
        return f'{self.id} {self.go} {self.po}'

def Miope(objetos, cmax: int, inicial = ...):
    solucion, peso = ([inicial], inicial.po) if inicial != ... else ([], 0)

    objetosOrdenados = sorted(objetos, key=lambda o: o.go/o.po, reverse=True)
    for objeto in objetosOrdenados:
        if peso + objeto.po <= cmax:
            solucion.append(objeto)
            peso += objeto.po
        if peso == cmax:
            break
    return solucion

def Greedy(archivo: str, puntoDePartida: int = ...):
    inicial = ...
    with open(archivo, 'r') as puntero:
        objetos = []
        _, cmax = map(int, puntero.readline().strip().split(' '))
        for linea in puntero:
            objeto = Objeto(*map(int, linea.strip().split(' ')))
            if objeto.id == puntoDePartida:
                inicial = objeto
            else:
                objetos.append(objeto)
    solucion = Miope(objetos, cmax, inicial)
    print(reduce(lambda a, o: a + o.go, solucion, 0), reduce(lambda a, o: a + o.po, solucion, 0))
    return solucion 

def main():
    print(Greedy('f1_l-d_kp_10_269.txt'))

if __name__ == '__main__':
    main()
