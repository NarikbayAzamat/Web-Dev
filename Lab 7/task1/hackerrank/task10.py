students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = [s[1] for s in students]

unique_scores = sorted(set(scores))

second_lowest = unique_scores[1]

result = [s[0] for s in students if s[1] == second_lowest]

result.sort()
for name in result:
    print(name)