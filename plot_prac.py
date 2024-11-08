import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.random.randn(50).cumsum(), 'k--')
plt.show()

plt.subplot(1, 2, 1)
plt.subplot(122)
plt.show()

plt.subplot(2, 2, 1)
plt.plot(np.random.randn(50).cumsum(), 'k--')
plt.subplot(2, 2, 2)
plt.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
plt.subplot(2, 2, 3)
plt.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.show()