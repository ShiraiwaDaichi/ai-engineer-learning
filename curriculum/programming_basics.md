# プログラミング基礎カリキュラム
<!-- ここでは文法から設計・パフォーマンスまで幅広く学びます -->

以下では、プログラミングの基礎を段階的に学ぶためのカリキュラムをまとめます。それぞれのセクションには、ビジネス分野およびゲーム開発分野での具体的なユースケース例を挙げ、実践に活かせる形で理解を深めます。

## 1. 言語の文法・構文
- 変数、データ型、演算子
- 条件分岐（`if`、`switch`）
- ループ（`for`、`while`）
- 関数定義と呼び出し

**ビジネスでの活用例**
- データ集計・変換スクリプトの自動化
- 簡易レポート生成ツールの作成

**ゲーム開発での活用例**
- プレイヤー入力の処理ループ
- NPC の行動分岐ロジック

### サンプルコード (Python)
```python
x = 10  # 変数へ数値を代入
if x > 5:  # 条件分岐
    print("greater")  # 条件が真の場合の処理

for i in range(3):  # 0 から 2 までループ
    print(i)

def greet(name):
    return f"Hello {name}"  # 文字列を返す関数
```
## 2. 標準ライブラリと組み込み関数
- 文字列操作、ファイル入出力、日付処理
- データ構造（配列、リスト、辞書 など）

**ビジネスでの活用例**
- ログファイルを読み込み解析するツール
- CSV/JSON 形式データのインポート・エクスポート

**ゲーム開発での活用例**
- レベルデータの読み込み・保存
- ゲーム設定ファイルのパース

### サンプルコード (Python)
```python
from datetime import datetime
with open('example.txt', 'w') as f:  # ファイルを開いて書き込み
    f.write('Hello')

print(datetime.now().strftime('%Y-%m-%d'))  # 今日の日付を表示
```
## 3. 抽象化（モジュール化・関数化）
- コードを責任ごとに分割
- 再利用できる関数・クラスの設計

**ビジネスでの活用例**
- REST API クライアントライブラリの実装
- 分析処理を共通モジュールとして切り出す

**ゲーム開発での活用例**
- キャラクター操作をコンポーネント化
- 共通 UI 部品のライブラリ化

### サンプルコード (Python)
```python
def add(a, b):
    return a + b  # 2つの値を足す関数

class Greeter:
    def __init__(self, name):
        self.name = name  # インスタンス変数に保存
    def greet(self):
        return f"Hello {self.name}"

print(add(2, 3))  # 5 を表示
print(Greeter('Alice').greet())  # クラスメソッド呼び出し
```
## 4. データ構造とアルゴリズム
- 配列、連結リスト、スタック・キュー、ハッシュテーブル
- ソート・探索アルゴリズムの選択
- 計算量（Big-O）を意識した実装

**ビジネスでの活用例**
- 大量データからの高速検索エンジン
- 優先度付きタスク管理システム

**ゲーム開発での活用例**
- 経路探索（A* など）による AI 移動
- 当たり判定用空間分割データ構造

### サンプルコード (Python)
```python
numbers = [3, 1, 4]
numbers.sort()  # 配列を昇順に並べ替え
print(numbers)

def binary_search(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # 見つからない場合

print(binary_search(numbers, 4))  # 4 の位置を表示
```
## 5. テスト駆動開発とデバッグ
- 単体テスト、統合テストの基礎
- デバッガやログ出力の使い方

**ビジネスでの活用例**
- 業務ロジックの変更時にリグレッションテストを自動実行
- 例外発生時のログからバグの原因を特定

**ゲーム開発での活用例**
- ゲームルールの検証をユニットテストで自動化
- フレーム毎の状態をログ出力してタイミングバグを調査

### サンプルコード (Python)
```python
import unittest  # 標準テストフレームワーク

def add(a, b):
    return a + b  # 被テスト関数

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # 成功するテストケース

if __name__ == '__main__':
    unittest.main(exit=False)  # テスト実行エントリ

try:
    add('1', 2)  # 意図的に型を間違えて例外を確認
except Exception as e:
    print('Error:', e)  # エラーメッセージを表示
```
## 6. 設計原則（SOLID・DRY・KISS など）
- 単一責任の原則 (SRP)
- 依存関係逆転の原則 (DIP)
- 重複排除 (DRY)、シンプルさ重視 (KISS)

**ビジネスでの活用例**
- モジュール依存を減らし保守性の高いサービス設計
- 共通処理をライブラリ化して重複コードを削減

**ゲーム開発での活用例**
- ゲームロジックをコンポーネント化し拡張を容易に
- スクリプト中の重複イベント処理をまとめてシンプル化

### サンプルコード (Python)
```python
class Logger:
    def log(self, msg):
        print(msg)  # 依存先の処理

class Game:
    def __init__(self, logger):
        self.logger = logger  # 依存性の注入
    def start(self):
        self.logger.log('game start')  # Logger に処理を委任

Game(Logger()).start()  # 実行例
```
## 7. ツールチェーンとワークフロー
- Git を用いたバージョン管理
- CI 環境での自動テスト
- パッケージ管理ツール（npm、pip など）

### サンプルコード
```bash
# Git 初期化とテスト実行
git init                                 # 新規リポジトリを作成
pip install -r requirements.txt          # 依存パッケージのインストール
pytest                                   # テストを実行
```
```yaml
# .github/workflows/test.yml
name: ci  # ワークフロー名
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: pip install -r requirements.txt  # 依存をインストール
      - run: pytest  # テスト実行
```
**ビジネスでの活用例**
- 新機能追加時にプルリクエスト＋CI で品質を確保
- Docker を使って同一の開発・本番環境を再現

**ゲーム開発での活用例**
- ソースコードとアセットを Git で一元管理
- 自動ビルドパイプラインで各プラットフォーム向けにデプロイ

## 8. 言語内部の仕組みとパフォーマンス
- メモリ管理、ガベージコレクションの理解
- 非同期 I/O と並行処理
- プロファイリングによるボトルネック特定

**ビジネスでの活用例**
- 大量リクエストを捌く Web サービスの最適化
- メモリリークを避けた長時間稼働バッチ処理

**ゲーム開発での活用例**
- フレームレート維持のためのメモリ管理最適化
- ネットワーク同期処理のレイテンシ削減

### サンプルコード (Python)
```python
import asyncio  # 非同期処理モジュール

async def fetch_data():
    await asyncio.sleep(1)  # 1 秒待つ
    return 'data'

asyncio.run(fetch_data())  # イベントループで実行

import sys
items = [0] * 1000  # メモリ使用量の例
print(sys.getsizeof(items))  # バイト数を表示
```
## 9. 他人のコード理解とレビュー
- コードリーディングのポイント（命名、コメント、設計パターン）
- 建設的なコードレビューの実践

**ビジネスでの活用例**
- 他チームが書いたモジュールを素早く理解し、バグ修正や機能追加を担当
- レビューでテスト観点や設計改善を提案し、品質向上に貢献

**ゲーム開発での活用例**
- 既存ゲームエンジンのコードを読み、新しいゲームシステムを拡張
- プルリク時にパフォーマンスや設計を意識したフィードバックを行う

### サンプルコード (Python)
```python
def multiply(x, y):
    """Return product of x and y."""
    return x * y  # 掛け算を行う

# TODO: overflow 対応を検討  # 改善点をコメントとして残す
```
---

このカリキュラムを順に学習することで、文法知識だけでなく問題へのアプローチ力を体系的に身につけられます。ビジネス分野・ゲーム開発分野の両面での活用例に触れることで、より実践的な視点から知識を定着させましょう。
