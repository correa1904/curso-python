import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
empresa_a = np.random.random(10) * 100
empresa_b = np.random.random(10) * 100

plt.plot(empresa_a, label='empresa1', c="black")

plt.plot(empresa_b, 'blue', label='empresa2')
plt.legend(loc='upper center')

plt.show()