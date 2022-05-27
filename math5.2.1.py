res = {}
for i in range(0, 1000):
    x = round(np.random.uniform(0, 36))
    res[x] = res[x] + 1 if x in res else 0

summ = 0
for key in res.keys():
    summ += 1 / len(res.keys())

print(summ)
