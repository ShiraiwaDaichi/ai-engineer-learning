// 標準ライブラリ利用例: ファイル操作と日付取得 (Node.js)
const fs = require('fs');

fs.writeFileSync('example.txt', 'Hello'); // ファイルに書き込み

// 現在の日付を YYYY-MM-DD 形式で表示
console.log(new Date().toISOString().slice(0, 10));
