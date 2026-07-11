def sistema(Co, Zo, r, c, b, d, n):
    C = [Co]
    Z = [Zo]

    for _ in range(n):
        Cn = C[-1]
        Zn = Z[-1]

        C.append( Cn + r*Cn*(1-Cn) - b*Cn*Zn ) 
        Z.append( Zn - d*Zn + c*Zn*Cn)

    tiempos = range(n+1)
    point_x = d/c 
    point_y = (r*(c-d)) / (b*c)
    
    return tiempos, C, Z, point_x, point_y
