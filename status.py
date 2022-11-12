class Status():
    '''
    自キャラ、敵キャラ共通で使うステータス
    default*は通常時のステータス(レベルアップ以外で値が変わらない)
    それ以外は現在のステータス(戦闘等によって値が変わる)
    '''
    hp: int
    defaultHP: int
    mp: int
    defaultMP: int
    attack: int
    defaultAtk: int
    defence: int
    defaultDef: int
    magic: int
    defaultMag: int
    speed: int
    defaultSpd: int
    
    def __init__(self, hp: int, mp: int, attack: int, defence: int, magic: int, speed: int) -> None:
        self.hp = hp
        self.defaultHP = hp
        self.mp = mp
        self.defaultMP = mp
        self.attack = attack
        self.defaultAtk = attack
        self.defence = defence
        self.defaultDef = defence
        self.magic = magic
        self.defaultMag = magic
        self.speed = speed
        self.defaultSpd = speed

    def show(self) -> None:
        '''
        現在のステータスを標準出力するメソッド
        '''
        print(f"hp: {self.hp}, mp: {self.mp} \nattack: {self.attack}, defence: {self.defence} \nmagic: {self.magic}, speed: {self.speed}")