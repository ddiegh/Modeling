import matplotlib.pyplot as plt
import modelo


def f(X):
    return X[0]**2 + 3*X[1]**2

def main():
    print(modelo.alg_evolutivo(f, [-2, 4], 1, 0.2, [-10, 10], [-10, 10], 10))

    
if __name__ == "__main__":
    main()



