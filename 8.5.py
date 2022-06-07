A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])
np.linalg.lstsq(A, B, rcond=None)

#(array([ 1.38191882, -0.18081181,  0.0202952 ]),
# array([], dtype=float64),2,
# array([9.65316119, 2.41173777]))

from matplotlib import pyplot as plt

def Q(x, y, z):
    return (x**2 + y**2 + z**2)

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)

Z = Q(X, Y, x + (2*y) - 1)

ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color="red")
show()
