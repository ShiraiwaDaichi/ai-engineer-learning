// 依存性注入を利用したクラス設計例
class Logger {
  log(msg) {
    console.log(msg);
  }
}

class Game {
  constructor(logger) {
    this.logger = logger;
  }
  start() {
    this.logger.log('game start');
  }
}

new Game(new Logger()).start();
