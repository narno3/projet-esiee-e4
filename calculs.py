import math
import scipy.constants as constants

hauteur = 5 * 10e-2  # distance au plan de masse

d1 = 0.5 * 10e-3  # diametre cable 1
d2 = 2 * 10e-3  # diametre cable 2

longueur_ligne_1 = 5  # longueur ligne 1
longueur_ligne_2 = 5  # longueur ligne 2


def get_l_c(h: int, d: int):
    """
    retourne L et C pour un cable de diamètre 'd'
    élevé d'une hauteur 'h' à un plan de masse
    """
    l = (constants.mu_0 / (2 * math.pi)) * math.log((4 * h - d) / d)
    c = (2 * math.pi * constants.epsilon_0) / math.log((4 * h - d) / d)
    return l, c


def get_mutual_inductance(): ...
    

def get_l_c_bifilaire(): ...


# valeurs linéiques

l1, c1 = get_l_c(hauteur, d1)
l2, c2 = get_l_c(hauteur, d2)


print(f"cable de données : L1 : {l1}, C1 : {c1}")
print(f"cable de puissance : L2 : {l2}, C2 : {c2}")
