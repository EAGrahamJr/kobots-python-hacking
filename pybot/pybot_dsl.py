class MoverFactory:
    @staticmethod
    def servo(motor)->DSLMover:
        pass

class DSLMover():
    _duration = 0.0

    def __init__(self, mover:BaseMover):
        self._mover = mover

    @duration.setter
    def duration(self,value):
        self._duration = value

    def smoothly():
        # moves to the requested location with a soft start and landing
        # this is the actual "activation" method
        pass
