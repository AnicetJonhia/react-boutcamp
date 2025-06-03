"""calcul  de déterminant matriciel """
# avec numpy
import numpy as np

# Définir la matrice 3x3
matrice = np.array([[2, 1, 3],
                    [4, 1, 2],
                    [3, 0, 1]])

# Calcul du déterminant
determinant = np.linalg.det(matrice)

print("Déterminant :", round(determinant)) 

# manuel 

"""
| a b c |
| d e f |
| g h i |

"""

def determinant_3x3(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return a * (e*i - f*h) - b * (d*i - f*g) + c * (d*h - e*g)

# Exemple
matrice = [
    [2, 1, 3],
    [4, 1, 2],
    [3, 0, 1]
]

det = determinant_3x3(matrice)
print("Déterminant :", det)

