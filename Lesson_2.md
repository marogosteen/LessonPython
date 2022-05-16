# 反復 while
### 以下のプログラムをdemo_while.pyに記述し実行．
```
#強制終了はControl + C
counter = 10
while counter > 0:
    print(counter)
    counter -= 1

print('Happy new year！')
```

`while`は`if`同様，Boolean型から処理を反復するのかを判断している．上記の例ではあらかじめ`counter = 10`とし，`counter`が0以下になるまで`counter - 1`を反復している．反復処理から抜けるとHappy new year！と出力した．<br>
`while`は条件以外にも，`break`でも反復を停止させられる．以下のプログラムは`break`を用いた例である．上記の例と同じ処理をしている．
```
#強制終了はControl +C
counter = 10
while True:
    if counter <= 0:
        break

    print(counter)
    counter -= 1

print('Happy new year！')
```

こちらの場合は`while`の評価は常に`True`であるため無限に反復する．そのため，分岐によって`counter`が0以下となれば`break`によって反復を停止させた．

以下のプログラムで無限ループを試す．強制終了はControl + C．
```
while True:
    print("hoge")
```

## 練習問題
テストの点数を任意の回数入力し，入力したデータから合計点と平均点を出力するプログラムを作りなさい．<br>
プログラムの条件は以下の通り．
- 点数を入力できるように標準入力を用いる．
- whileを使い，任意の回数入力できるようにする．
- 入力が999である時，反復を抜けて結果(合計と平均)を表示する．

[ヒント](https://github.com/marogosteen/LessonPython/blob/master/code_sample/lesson2/hint_calc_score.py)<br>
[解答例](https://github.com/marogosteen/LessonPython/blob/master/code_sample/lesson2/ans_calc_score.py)

## 課題
あなたは自動販売機のプログラムを作ることになりました．代金と入力された金額から小銭の枚数が最小となるように，小銭の枚数を出力しなさい．<br>
条件は以下の通り．
- 商品の最安値は100円である．
- 標準入力から代金と入力金額を入力できる．
- この自販機は1円玉と5円玉を受け付けない．
- 販売されている商品の代金は必ず10で割り切れる．
- 購入ごとに追加購入するかユーザーに選択させる．

### できた人は以下の条件も追加してみる．
- 代金が足りない場合は，お釣りの計算に移行する．
- お釣りが100円未満になるまで任意の回数購入できるようにする．

[ヒント](https://github.com/marogosteen/LessonPython/blob/master/code_sample/lesson2/hint_vending_machine.py)<br>
[解答例](https://github.com/marogosteen/LessonPython/blob/master/code_sample/lesson2/ans_vending_machine.py)