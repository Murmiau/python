from matplotlib import pyplot as plt

res = []

x0 = np.random.randint(0, 37, 10)
x1 = np.random.randint(0, 37, 10)
x2 = np.random.randint(0, 37, 10)
x3 = np.random.randint(0, 37, 10)
x4 = np.random.randint(0, 37, 10)
x5 = np.random.randint(0, 37, 10)
x6 = np.random.randint(0, 37, 10)
x7 = np.random.randint(0, 37, 10)
x8 = np.random.randint(0, 37, 10)
x9 = np.random.randint(0, 37, 10)

x = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9

plt.hist(x, 5)
plt.xlabel("Сумма")
plt.ylabel("Вероятность")
plt.title("Гистограмма")
plt.show()
