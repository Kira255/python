data = [1, 2, 2, 2, 1, 1, 3]
popular = []

for i in range(len(data) - 1):
    for j in range(len(data) - 1):
        if data[i] == data[j]:
            popular.append(data[j])

valResult = data[0]
popResult = popular[0]
for i in range(len(data)):
    if popular[i] > popResult:
        popResult = popular[i]
        valResult = data[i]
    if (popResult == popular[i]) and (data[i] < valResult):
        valResult = data[i]
print(valResult)
