print("構造力学の点数を入力してください．")
a = int(input())

print("土質力学の点数を入力してください．")
b = int(input())

print("水理学の点数を入力してください．")
c = int(input())

h = (a+b+c)/3

if h < 60:
    print("D")
elif h < 70:
    print("C")
elif h < 80:
    print("B")
elif h < 90:
    print("A")
else:
    print("S")