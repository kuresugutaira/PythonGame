from lib.scenes.iscene import IScene
from lib.scenes.start_scene import StartScene
from lib.scenes.quit_scene import QuitScene
from typing import cast
import sys

class SceneLoader():
    '''
    各シーンを順々に呼び続けるクラス
    '''
    nextScene: IScene

    def __init__(self) -> None:
        pass

    def PlayGame(self) -> None:
        # StartSceneの読み込み
        startScene: StartScene = StartScene()
        startScene.EnterScene()
        startScene.SceneLoop()
        tmpScene = startScene.ExitScene()
        if tmpScene is None:
            self.ExitOnLoadNoneScene()
        self.nextScene = cast(IScene, tmpScene)
        # 以降順々にシーンの読み込み
        while True:
            self.nextScene.EnterScene()
            self.nextScene.SceneLoop()
            tmpScene = self.nextScene.ExitScene()
            # nextSceneの返り値がNoneのとき、ループを終了
            if tmpScene is None:
                break
            self.nextScene = cast(IScene, tmpScene)

    def ExitOnLoadNoneScene(self) -> None:
        print("上手くシーンが読み込めなかったためゲームを終了します。")
        sys.exit()