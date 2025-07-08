# ユニットテストの書き方を学ぶサンプル
import unittest

def add(a, b):
    """単純な加算関数"""
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        # add(1, 2) の結果が 3 になることを確認
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main(exit=False)  # テスト実行
