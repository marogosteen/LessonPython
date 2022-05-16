print("お金を入力してください．")
money = int(input())

while True:
    # 代金の入力
    print("商品の代金を入力してください．")
    price = int(input())

    # 代金が不足しているか判定
    if money - price < 0:
        print("お金が足りません．")
        break

    money = money - price

    # 残り金額が100円未満か判定
    if money < 100:
        break

    # 購入を続けるか
    print("購入を終えますか？ yes:y, no:n")
    isDone = input()
    if isDone == "y":
        break

change = money

print("500円玉", change // 500, "枚")
change = change - change // 500 * 500
print("100円玉", change // 100, "枚")
change = change - change // 100 * 100
print("50円玉", change // 50, "枚")
change = change - change // 50 * 50
print("10円玉", change // 10, "枚")
change = change - change // 10 * 10
