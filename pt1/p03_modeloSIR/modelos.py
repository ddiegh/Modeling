#susceptibles
def Sistema(So, Io, Ro, alfa, beta, n):
    
    S = [So]
    I = [Io]
    R = [Ro]

    N = So + Io + Ro

    for _ in range(n):
        Sn = S[-1]
        In = I[-1]

        S.append(Sn - (alfa*Sn*In)/N)
        I.append(In + (alfa*Sn*In)/N - beta*In)
        R.append(N-S[-1]-I[-1])

    return S, I, R

def R_o(alfa,So,N,beta):
    return (alfa*So) / (N*beta)
