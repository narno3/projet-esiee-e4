import math
import scipy.constants as constants

hauteur = 5*10e-2 # distance au plan de masse

d1 = 0.5 * 10e-3 # diametre cable 1
d2 = 2 * 10e-3 # diametre cable 2


def get_l_c(h: int, d: int):
    """
    retourne L et C pour un cable de diamètre 'd' 
    élevé d'une hauteur 'h' à un plan de masse
    """
    l = (constants.mu_0/2*math.pi) * math.log( (4*h - d) /d)
    c = (2*math.pi*constants.epsilon_0) / math.log( (4*h - d) /d)
    return l, c

def get_l_c_bifilaire():
    ...

l1, c1 = get_l_c(hauteur, d1)
l2, c2 = get_l_c(hauteur, d2)

print(f"cable de données :\n\tL1 : {l1}\n\tC1 : {c1}")
print(f"cable de puissance :\n\tL2 : {l2}\n\tC2 : {c2}")