# 非同期処理の基本例
import asyncio

async def fetch_data():
    """1 秒待ってから文字列を返す非同期関数"""
    await asyncio.sleep(1)
    return 'data'

asyncio.run(fetch_data())  # イベントループで実行
