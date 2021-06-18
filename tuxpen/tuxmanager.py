from tuxcore import tuxcore
from tuxboard import tuxboard


class TuxManager:
    def __init__(self):
        self.coreWindow = tuxcore.TuxCore(self)
        self.boardWindow = tuxboard.TuxBoard(self)
