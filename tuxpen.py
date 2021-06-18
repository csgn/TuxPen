#!/usr/bin/env python

import os
import sys

from pathlib import Path

MAIN_DIR = Path(__file__).resolve().parent.parent


def main():
  try:
    from tuxcore.tuxcore import execute
  except ImportError as exc:
    raise ImportError(
      "Couldn't import Tuxpen"
    )
  
  execute(sys.argv)


if __name__ == '__main__':
  main()