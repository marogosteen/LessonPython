class_count = 5

scores = []
row = 0
with open("test_score.csv", "r") as f:
    while True:
        row = row + 1
        # １行をlistに直す
        line = f.readline()

        # 最初の１行は無視
        if row != 1:
            if line == [""]:
                break

            # １行をcastingしてscoresに追加

# 何人いるのか計算（問題文に人数が載っているのでハードコードでも良い．）
people_count = len(scores)

# 一人ずつ合計点と平均点を計算，結果の追加
for row in range(0, people_count):
    line = scores[row]

# 科目毎の合計
sum_line = []
for col in range(0, class_count):
    sum_value = 0
scores.append(sum_line)

# 科目毎の平均
mean_line = []

with open("test_score.csv", "w") as f:
    for line in scores:
        str_line = []
        for num in line:
            str_line.append(str(num))
        f.write(",".join(str_line)+"\n")
