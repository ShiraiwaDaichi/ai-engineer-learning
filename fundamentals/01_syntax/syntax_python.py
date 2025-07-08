# このスクリプトでは条件分岐・ループ・関数定義といった基本文法を学習できます。

x = 10  # 数値変数の宣言
if x > 5:  # if 文による条件分岐
    print("greater")  # 条件が真のときに表示

for i in range(3):  # 0 から 2 まで繰り返し処理
    print(i)

def greet(name):
    """名前を受け取り挨拶文字列を返す関数"""
    return f"Hello {name}"

print(greet("Alice"))  # 関数の呼び出し例
