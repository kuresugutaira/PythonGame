from abc import ABCMeta, abstractmethod
from typing import Optional

class IScene(metaclass=ABCMeta):
    '''
    Sceneのインターフェイスクラス
    '''
    @abstractmethod
    def EnterScene(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def SceneLoop(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def ExitScene(self) -> Optional['IScene']:
        raise NotImplementedError()
