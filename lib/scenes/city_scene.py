from lib.scenes.iscene import IScene
from lib.scenes.quit_scene import QuitScene
from typing import Optional

class CityScene(IScene):
    '''
    街のシーン\n
    1: 冒険に出かける
    2: クラスチェンジする
    3: アイテムを買う
    4: ゲームを終わる\n
    から行動を選べる。
    '''
    nextScene: IScene

    def EnterScene(self):
        print("あなたは街に入った")
        return

    def SceneLoop(self) -> None:
        self.nextScene = QuitScene()
        return
    
    def ExitScene(self) -> Optional[IScene]:
        print("あなたは街を後にした")
        return self.nextScene