import numpy as np

#  0 = sushi, 1 = fc, 2 = pizza, 3 = indian
options = ["sushi", "fc", "pizza", "indian"]
votes = []
votes.append([0, 1, 2, 3])
votes.append([0, 1, 2, 3])
votes.append([1, 0, 2, 3])
votes.append([2, 1, 3, 0])

relations = {}
edges = len(options) * (len(options)-1)
for i in range(len(options)):
    for j in range(len(options)):
        relations[str(i) + "+" + str(j)] = 0

for i in range(len(votes)):
    for j in range(len(votes[i])):
        for y in range(j + 1, len(votes[i])):
            relations[str(votes[i][j]) + "+" + str(votes[i][y])] += 1/12
            relations[str(votes[i][j]) + "+" + str(votes[i][j])] += 1/12

probs = np.array(list(relations.values()))
probs = probs.reshape(-1, len(options))
print(probs)

result = np.full((len(options)), 1/len(options))
print(result)
avg_change = 1
while avg_change > 0.0001:
    tmp_change = 0
    temp = result
    result = probs.dot(result)
    for i in range(len(temp)):
        tmp_change += abs(temp[i]-result[i])
    avg_change = tmp_change / len(temp)

print(result)

