import numpy as np

l1 = np.arange(1, 20, 2)
l2 = np.arange(1, 100, 10)

print(l1)
print(l2)

n = int(input(f'Digite um número:'))

print((l1 + l2) * n)
