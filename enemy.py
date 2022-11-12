from abc import ABCMeta, abstractmethod
from status import Status
from player import Player

class Enemy(metaclass=ABCMeta):

    status: Status
    enemyName: str

    def Attack(self, target: Player) -> None:
        '''
        プレイヤーのステータスを参照し破壊的に変更する(HPを減らす)
        '''
        # Todo: ダメージ計算は計算クラスを用意してそっちに任せたい
        damage: int = self.status.attack - target.status.defence
        if damage <= 0:
            print(f"{self.enemyName}は{target.name}にダメージを与えられなかった")
            return
        else:
            print(f"{self.enemyName}は{target.name}に{damage}ダメージを与えた")
