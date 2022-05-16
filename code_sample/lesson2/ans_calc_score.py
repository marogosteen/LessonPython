sum_score = 0
counter = 0
while True:
    print("テストの点数を入力してください．")
    score = int(input())
    if score == 999:
        break

    counter = counter + 1
    sum_score = sum_score + score

print(sum_score/counter)
