// 非同期処理の基本例 (Node.js)
async function fetchData() {
  return new Promise(resolve => {
    setTimeout(() => resolve('data'), 1000);
  });
}

fetchData().then(console.log);
