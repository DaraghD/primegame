import sympy as pm

def mPrime(n1, n2, n3):
    p1 = n1 * 100 + n2 * 10 + n3
    p2 = n1 * 100 + n3 * 10 + n2
    p3 = n2 * 100 + n1 * 10 + n3
    p4 = n2 * 100 + n3 * 10 + n1
    p5 = n3 * 100 + n1 * 10 + n2
    p6 = n3 * 100 + n2 * 10 + n1
    return p1, p2, p3, p4, p5, p6

def ifPrime(n1, n2, n3, n4, n5, n6):
    ifPrimelist = []
    g1 = pm.isprime(n1)
    if g1 == True:
        ifPrimelist.append(n1)

    g2 = pm.isprime(n2)
    if g2 == True:
        ifPrimelist.append(n2)

    g3 = pm.isprime(n3)
    if g3 == True:
        ifPrimelist.append(n3)

    g4 = pm.isprime(n4)
    if g4 == True:
        ifPrimelist.append(n4)

    g5 = pm.isprime(n5)
    if g5 == True:
        ifPrimelist.append(n5)

    g6 = pm.isprime(n6)
    if g6 == True:
        ifPrimelist.append(n6)
    return ifPrimelist

#ifPrimelist - contains the primes - basically answerlist