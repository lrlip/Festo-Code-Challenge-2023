import time
import functools
from collections import deque
import datetime
from typing import Any

from utils.keyforger import KeyForger


filename = 'static/31_keymaker_forge_2.txt'
keyforger = KeyForger(filename=filename)

key = keyforger.solve(show_idx=True)
print(key)
