#!/usr/bin/env python

import sys


def main() -> None:
    try:
        from tuxcore import tuxcore
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Tuxpen"
        )

    tuxcore.execute(sys.argv)


if __name__ == '__main__':
    main()
