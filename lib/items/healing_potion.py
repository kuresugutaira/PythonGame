from lib.items.items import Item, ItemType
from status import Status

class HealingPotion(Item):
    '''
    体力をやや回復するアイテム
    '''
    itemType: ItemType = ItemType.HP_HEAL
    itemName: str = "回復ポーション"
    itemDescribe: str = "飲むとHPがすこし回復する"

    def ItemEffect(self, status: Status) -> None:
        status.hp += 15
        return
    
    def ShowFlavorText(self) -> None:
        print("あなたは爽快な気分になった")
        return