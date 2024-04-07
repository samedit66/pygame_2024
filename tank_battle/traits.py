class IsAlive:

    def __init__(self):
        self._is_alive = True

    def is_alive(self):
        return self._is_alive

    def die(self):
        self._is_alive = False

class SelfMoving:
    def move(self):
        raise NotImplementedEroor()