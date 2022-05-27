import itertools
import math

count, k, n, numb = 0, 3, 5, 100000

a = np.random.randint(0, 2, numbers)
b = np.random.randint(0, 2, numbers)
c = np.random.randint(0, 2, numbers)
d = np.random.randint(0, 2, numbers)
e = np.random.randint(0, 2, numbers)

x = a + b + c + d + e

for i in x:
    if x[i] == k:
        count += 1
print(count, numb, count / numb)

cnk = math.factorial(n) / (math.factorial(n - k) * math.factorial(k))
pnk = cnk * ((k / n) ** k) * ((1 - k / n) ** (n - k))

print("Вероятность по Монте-Карло:", count / numb)
print("Вероятность по Бернулли:", pnk)
