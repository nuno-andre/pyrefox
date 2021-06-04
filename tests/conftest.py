from pathlib import Path
import sys

BASEDIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASEDIR / 'src'))

import pyrefox  # noqa: E402, F401
