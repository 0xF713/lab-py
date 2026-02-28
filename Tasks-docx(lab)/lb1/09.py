import numpy as np

x = 1

result = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
print(result)