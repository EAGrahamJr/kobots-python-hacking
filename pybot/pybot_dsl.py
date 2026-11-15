
from pybot.pybot_mover import BaseMover


class DSLMover():
    _duration = 0.0

    def __init__(self, mover:BaseMover):
        self._mover = mover

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self,value):
        self._duration = value

    def smoothly(self):
        # moves to the requested location with a soft start and landing
        # this is the actual "activation" method
        pass

class MoverFactory:
    @staticmethod
    def servo(motor)->DSLMover | None:
        pass
