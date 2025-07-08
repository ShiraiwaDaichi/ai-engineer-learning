// ソートと二分探索の例
const numbers = [3, 1, 4];
numbers.sort((a, b) => a - b);
console.log(numbers);

function binarySearch(data, target) {
  let low = 0;
  let high = data.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (data[mid] === target) return mid;
    if (data[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}

console.log(binarySearch(numbers, 4));
