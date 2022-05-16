print("お金を入力してください．")
money = int(input())

while True:
    # 代金の入力
    print("商品の代金を入力してください．")
    price = int(input())

    # 購入を続けるか
    print("購入を終えますか？ yes:y, no:n")
    isDone = input()
    if isDone == "y":
        break

change = money

# 小銭計算