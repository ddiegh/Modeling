import gauss_jordan
import lu
import qr

matriz_prueba_diag = [
    [2.0,  1.0, -1.0],
    [4.0,  5.0,  0.0],
    [2.0, -2.0, -1.0]
]

matriz_lu = [
    [ 2.0,  1.0, -1.0],
    [ 4.0,  5.0,  0.0],
    [-2.0,  8.0,  9.0]
]

matriz_qr = [
    [ 2.0,  1.0,  3.0],
    [ 2.0,  4.0,  3.0],
    [-1.0,  1.0,  3.0]
]

def main():
    print('----'*30)
    diag = gauss_jordan.gauss_jordan(matriz_prueba_diag)
    print(f"el algoritmo de diagonalizacion usando gauss-jordan nos dio: {diag}")

    print('----'*30)
    m_lu = lu.lu(matriz_lu)
    print(f"la descomposicion lu nos dio: {m_lu}")

    print('----'*30)
    m_qr = qr.qr(matriz_qr)
    print(f"la descomposicion qr nos dio: {m_qr}")

if __name__ == "__main__":
    main()
