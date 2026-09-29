#Bài 2:

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z = np.linspace(-8, 8, 50)
gia_tri = sigmoid(z)

plt.plot(z, gia_tri)
plt.title("Đồ thị hàm sigmoid")
plt.axhline(y=0.5, color='r', linestyle='--', label='y=0.5')
plt.axvline(x=0, color='g', linestyle=':', label='z=0')
plt.xlabel("z")
plt.ylabel("sigmoid(z)")
plt.legend()

plt.savefig('sigmoid.png')
plt.show()