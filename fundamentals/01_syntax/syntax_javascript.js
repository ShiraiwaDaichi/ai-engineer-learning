// 条件分岐・ループ・関数定義の基礎例
let x = 10; // 数値変数の宣言
if (x > 5) {
  console.log('greater'); // 条件が真なら出力
}

for (let i = 0; i < 3; i++) { // 0 から 2 までループ
  console.log(i);
}

function greet(name) {
  // 引数 name を使って挨拶を返す関数
  return `Hello ${name}`;
}

console.log(greet('Alice')); // 関数呼び出し例
