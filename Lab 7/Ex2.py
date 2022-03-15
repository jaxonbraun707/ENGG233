a = [101, 102, 103, 104]
b = [2, 3, 4]
allItems = []
i = 0

for i in range(0, len(a)):
    allItems.append(a[i])

for j in range(0, len(b)):
    allItems.append(b[j])
    i += 1

for i in range(0, (len(a) + len(b))):
    print(allItems[i])
