from abc import ABCMeta, abstractmethod
from enum import Enum
from status import Status

class ItemType(Enum):
    HP_HEAL = 1
    MAGIC_HEAL = 2
    BUFF = 3
    NERF = 4
    ALL_NERF = 5
    DAMAGE = 6
    ALL_DAMAGE = 7

class Item(metaclass=ABCMeta):
    '''
    Itemの抽象クラス\n
    '''
    itemType: ItemType
    itemName: str
    itemDescribe: str

    def ShowUseText(self):
        print(f"{self.itemName}を使用した。")

    @abstractmethod
    def ItemEffect(self, status: Status) -> None:
        '''
        アイテムの効果を発動する
        playerStatusは参照を渡して破壊的に変更する
        '''
        raise NotImplementedError()

    @abstractmethod
    def ShowFlavorText(self) -> None:
        '''
        アイテムを使用した後のテキスト
        使用して得られた効果、使用した際の感想など
        '''
        raise NotImplementedError()

    def Use(self, status: Status):
        '''
        アイテム使用のフレーバーテキストを表示してから
        アイテムの効果を発動する
        '''
        self.ShowUseText()
        self.ItemEffect(status)
        self.ShowFlavorText()
        return
