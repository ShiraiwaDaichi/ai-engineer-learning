# このファイルでは関数とクラスを使った抽象化の例を示します

def add(a, b):
    """2つの値を足して返す単純な関数"""
    return a + b

class Greeter:
    """挨拶メッセージを生成するクラス"""
    def __init__(self, name):
        self.name = name  # インスタンス変数に名前を保持
    def greet(self):
        return f"Hello {self.name}"  # フォーマットした文字列を返す

print(add(2, 3))  # 関数呼び出し
print(Greeter('Alice').greet())  # クラス利用例
