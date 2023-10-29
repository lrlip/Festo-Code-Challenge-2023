import time
import functools
from collections import deque
import datetime
from typing import Any

from utils.keyforger import KeyForger


filename = 'static/21_keymaker_forge.txt'
keyforger = KeyForger(filename=filename)

key = keyforger.solve(show_idx=False)
print(key)
