import qr as model
from numpy import tril, sum, abs

def eigenvalores(A: list[list], iteraciones: int = 1000, tol: float = 1e-10):

    A_k = A

    for i in range(iteraciones):
        Q, R = model.qr(A_k)
        A_k = R.dot(Q)

        error = sum(abs(tril(A_k, -1)))
        if error < tol:
            print(f"Convergencia en {i} iteraciones")
            break
    return A_k


def main():
    A = [
    [3.0, -1.0,  1.0],
    [-1.0, 5.0, -1.0],
    [1.0, -1.0,  3.0]]

    print(eigenvalores(A))

if __name__ == "__main__":
    main()