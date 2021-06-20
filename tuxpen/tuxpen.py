#!/usr/bin/env python

import sys


def main() -> None:
    try:
        from PySide6 import QtWidgets
        from tuxmanager import TuxManager
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Tuxpen"
        )

    app = QtWidgets.QApplication(sys.argv)
    wm = TuxManager(app)
    wm.coreWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
