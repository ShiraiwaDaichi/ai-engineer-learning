# リストをソートし、二分探索を実装する例
numbers = [3, 1, 4]
numbers.sort()  # 標準のソート(Timsort)を利用
print(numbers)

def binary_search(data, target):
    """昇順リスト data から target の位置を探す"""
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2  # 範囲中央のインデックス
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # 見つからない場合

print(binary_search(numbers, 4))  # 結果: 2
