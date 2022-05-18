class_count = 5

scores = []
with open("test_score.csv", "r") as f:
    while True:
        line = f.readline().strip().split(",")
        if line == [""]:
            break

# 何人いるのか計算（問題文に人数が載っているのでハードコードでも良い．）
people_count = len(scores)

# 一人ずつ合計点と平均点を計算，結果の追加
for row in range(0, people_count):
    line = scores[row]

# 科目毎の合計
sum_line = []
for col in range(0, class_count):
    sum_value = 0
    for row in range(0, people_count):
        sum_value = sum_value + scores[row][col]

# 科目毎の平均
scores.append(sum_line)

mean_line = []

with open("test_score.csv", "w") as f:
    for line in scores:
        str_line = []
        f.write(",".join(str_line)+"\n")
