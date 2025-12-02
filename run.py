#!/usr/bin/env python
"""Launcher pour Quiz Champion"""

import sys
from pathlib import Path

# Ajoute src au PATH
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from quiz_champion.main import main

if __name__ == "__main__":
    main()
