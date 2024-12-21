# app/controllers/coin_flip_controller.py
import random

class CoinFlipController:
    def flip_coin(self):
        # Подброс монетки
        result = random.choice(["Орел", "Решка"])
        return result
