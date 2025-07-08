// 関数とクラスを使った抽象化例
function add(a, b) {
  return a + b;
}

class Greeter {
  constructor(name) {
    this.name = name;
  }
  greet() {
    return `Hello ${this.name}`;
  }
}

console.log(add(2, 3));
console.log(new Greeter('Alice').greet());
