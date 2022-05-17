class_count = 5

scores = []
row = 0
with open("test_score.csv", "r") as f:
    while True:
        row = row + 1
        line = f.readline().strip().split(",")
        if row != 1:
            if line == [""]:
                break

            score = []
            for point in line[1:]:
                score.append(int(point))

            scores.append(score)

people_count = len(scores)

for row in range(0, people_count):
    line = scores[row]
    sum_value = sum(line)
    mean_value = sum_value / len(line)
    scores[row].append(sum_value)
    scores[row].append(mean_value)

sum_line = []
for col in range(0, class_count):
    sum_value = 0
    for row in range(0, people_count):
        sum_value = sum_value + scores[row][col]
    sum_line.append(sum_value)
scores.append(sum_line)

mean_line = []
for score in scores[10]:
    mean_line.append(score/people_count)
scores.append(mean_line)

with open("test_score.csv", "w") as f:
    for line in scores:
        str_line = []
        for num in line:
            str_line.append(str(num))
        f.write(",".join(str_line)+"\n")
