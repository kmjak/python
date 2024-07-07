## リストの使い方

# リストの作成
a = [0, 1, 2, 3, 4]

# インデックスを使った取り出し方
print(a[0]) # aの0番目の要素を取り出す(0)
print(a[1]) # aの1番目の要素を取り出す(1)
print(a[2]) # aの2番目の要素を取り出す(2)
print(a[3]) # aの3番目の要素を取り出す(3)
print(a[4]) # aの4番目の要素を取り出す(4)
print()

# forを使った取り出し方
b = ["apple", "banana", "cherry", "date", "elderberry"]
for i in b:
    # bの要素を左から順にiに代入している
    print(i)
print()

## あんま使わないけど、あると便利なやつ
#　リストを使ったリストの取り出し方
for i in a:
    print(b[i])
print()

# len()を使ったリストの取り出し方
# len()はリストの要素数を返す
# つまり、rangeの中には、aの要素数の5が入り、range(5)となる
for i in range(len(a)):
    print(a[i])
print()
