# 設計原則の実例: 依存性注入を用いたクラス設計

class Logger:
    def log(self, msg):
        print(msg)

class Game:
    def __init__(self, logger):
        self.logger = logger  # Logger に依存するが外から注入
    def start(self):
        self.logger.log('game start')  # ロギング処理に委譲

Game(Logger()).start()  # 実行例
