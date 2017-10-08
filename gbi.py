
"""
simple Python3 script to demonstrate Graph Based Inversion
"""

import numpy as np

k = np.array([-1/4, 3/5, 2/3])

alphas = [k[0:1]]

for i in range(1, len(k)):
    mat1  = np.append(alphas[-1],0)
    mat2  = np.append(np.flip(alphas[-1],0),-1)
    alpha = mat1 - k[i] * mat2
    alphas.append(alpha)

for i, alpha_i in enumerate(alphas):
    print('alpha%d =' % (i+1), alpha_i)

print()

a = [-1] + list(alphas[-1])
for i,a_i in enumerate(a):
    print('a%d =' % i, -a_i)
