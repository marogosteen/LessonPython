print("以下の a b c から面積を求めたいものを入力してください．")
print("a. 三角形")
print("b. 円形")
print("c. 台形")

menu = input()

if menu == "a":
    print("底辺を入力してください．")
    b = int(input())

    print("高さを入力してください．")
    h = int(input())

    print("三角形の面積")
    print(b*h/2)

elif menu == "b":
    print("半径を入力してください．")
    r = int(input())

    print("円形の面積")
    print(3.14*r**2)

elif menu == "c":
    print("下辺を入力してください．")
    b = int(input())

    print("上辺を入力してください．")
    t = int(input())

    print("高さを入力してください．")
    h = int(input())

    print("台形の面積")
    print((b+t)*h/2)

else:
    print("a b cから選んでください．")
