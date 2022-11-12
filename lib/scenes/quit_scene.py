import sys
from lib.scenes.iscene import IScene
from lib.utils.color import Color
from typing import Optional

class QuitScene(IScene):
    '''
    最後に呼び出されるシーン
    '''

    def EnterScene(self) -> None:
        self.SceneLoop()
        return

    def SceneLoop(self) -> None:
        return

    def ExitScene(self) -> Optional[IScene]:
        print('遊んでいただきありがとうございました')
        return None