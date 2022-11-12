from lib.scenes.iscene import IScene
from lib.scenes.city_scene import CityScene
from typing import Optional

class StartScene(IScene):
    '''
    一番最初のシーン
    '''
    nextScene: IScene
    def EnterScene(self) -> None:
        return

    def SceneLoop(self) -> None:
        print('お名前を教えてください: ')
        self.nextScene = CityScene()
        return

    def ExitScene(self) -> Optional[IScene]:
        return self.nextScene