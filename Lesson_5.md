# Data visualize (matplotlib)

## matplotlib
ここでは，pythonとmatplotlibを使ってデータを可視化していく．pythonのmatplotlibはデータ可視化ライブラリである．<br>
ライブラリとは，第三者が再利用可能にしたソースコード群であり，matplotlibではグラフ関連の機能を提供されている．<br>
matplotlibの[公式ページ](https://matplotlib.org/stable/index.html)には，[Example集](https://matplotlib.org/stable/gallery/index.html)が用意されている．こちらから，実装したいものに近しいものを選んで参考にする．

### plot(折れ線グラフ)
matplotlibによるシンプルな折れ線グラフは[こちら](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py)を参照した．

```
import math

import matplotlib.pyplot as plt

t = []
s = []
for i in range(201):
    x = i * 0.01
    y = 2 * math.pi * x
    t.append(x)
    s.append(math.sin(y))

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")

```

### scatter(散布図)
plotで使用したソースコードを散布図にする．

```
import math

import matplotlib.pyplot as plt

t = []
s = []
for i in range(201):
    x = i * 0.01
    y = 2 * math.pi * x
    t.append(x)
    s.append(math.sin(y))

fig, ax = plt.subplots()
ax.scatter(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")

```

## 練習問題
アメダスより9/3から9/5までの神戸空港の風速を取得し，風速の折れ線グラフを画像ファイル（jpg）として保存せよ．