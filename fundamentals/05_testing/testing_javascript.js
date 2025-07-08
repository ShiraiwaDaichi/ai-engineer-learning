// テストの基礎例: Node.js の assert を利用
const assert = require('assert');

function add(a, b) {
  return a + b;
}

try {
  assert.strictEqual(add(1, 2), 3);
  console.log('test passed');
} catch (e) {
  console.error('test failed', e);
}
