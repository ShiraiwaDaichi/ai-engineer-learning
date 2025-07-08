# 標準ライブラリ利用例: ファイル操作と日付取得
from datetime import datetime

with open('example.txt', 'w') as f:  # ファイルを書き込みモードで開く
    f.write('Hello')  # テキストを書き込む

# 現在の日付を YYYY-MM-DD 形式で出力
print(datetime.now().strftime('%Y-%m-%d'))
