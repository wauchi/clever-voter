import numpy as np


class VotingCalculator:
    def __init__(self, categories, votes):
        self.categories = [x.strip(" ")for x in categories]
        self.votes = []
        for i in range(len(votes)):
            tmp = []
            for j in [x.strip(" ") for x in votes[i].split(',')]:
                tmp.append(self.categories.index(j))
            self.votes.append(tmp)

    def calculate(self):
        relations = {}
        edges = len(self.categories) * (len(self.categories) - 1)
        for i in range(len(self.categories)):
            for j in range(len(self.categories)):
                relations[str(i) + "+" + str(j)] = 0

        for i in range(len(self.votes)):
            for j in range(len(self.votes[i])):
                for y in range(j + 1, len(self.votes[i])):
                    relations[str(self.votes[i][j]) + "+" + str(self.votes[i][y])] += 1 / edges
                    relations[str(self.votes[i][j]) + "+" + str(self.votes[i][j])] += 1 / edges

        probs = np.array(list(relations.values()))
        probs = probs.reshape(-1, len(self.categories))
        print(probs)

        result = np.full((len(self.categories)), 1 / len(self.categories))
        print(result)
        avg_change = 1
        while avg_change > 0.0001:
            tmp_change = 0
            temp = result
            result = probs.dot(result)
            for i in range(len(temp)):
                tmp_change += abs(temp[i] - result[i])
            avg_change = tmp_change / len(temp)

        return self.build_result(result)

    def build_result(self, result_in):
        result_out = {}
        for i in range(len(result_in)):
            result_out[self.categories[i]] = result_in[i]
        return result_out

# #  0 = sushi, 1 = fc, 2 = pizza, 3 = indian
# options = ["sushi", "fc", "pizza", "indian"]
# votes = ["sushi,fc,pizza,indian","sushi,fc,pizza,indian","fc,sushi,pizza,indian","pizza,fc,indian,sushi"]
# # votes.append([0, 1, 2, 3])
# # votes.append([0, 1, 2, 3])
# # votes.append([1, 0, 2, 3])
# # votes.append([2, 1, 3, 0])
# test = VotingCalculator(options, votes)
# print(test.calculate())




