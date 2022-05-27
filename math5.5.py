n = 500
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, "o")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
a = np.corrcoef(x, y) 
print("Коэффициент корреляции через встроенную библиотеку:", a)

R = np.sum((x - x.mean()) * (y - y.mean())) / np.sqrt(np.sum((x-x.mean())**2) * np.sum((y-y.mean())**2))
print("Коэффициент корреляции по формуле:", R)
