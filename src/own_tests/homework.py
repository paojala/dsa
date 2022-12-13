def recursive(n):
    if n == 0:
        return 1
    else:
        result = 1 / (1 + recursive(n - 1))
        return result

# Test
xlist = []
ylist = []
for n in range(0,10):
    xlist.append(n)
    ylist.append(recursive(n))

import numpy as np
import matplotlib.pyplot as plt

plt.scatter(xlist,ylist)
plt.show()


# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()