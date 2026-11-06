# /// script
# dependencies = [
#   "pgzero"
# ]
# ///
import sys
import types

# 1. EMULATE THE THREADING ENGINE BEFORE PGZERO SEES IT
# This traps the tone.py line 80 error before it can crash Python 3.12
class SafeThread:
    def __init__(self, *args, **kwargs):
        pass
    def setDaemon(self, val):
        pass
    def start(self):
        pass

if 'threading' not in sys.modules:
    fake_threading = types.ModuleType('threading')
    fake_threading.Thread = SafeThread
    sys.modules['threading'] = fake_threading

# 2. EMULATE TIMEIT FOR THE INTERNAL GAME ENGINE CLOCK
if 'timeit' not in sys.modules:
    fake_timeit = types.ModuleType('timeit')
    fake_timeit.default_timer = lambda: 0.0
    sys.modules['timeit'] = fake_timeit

import pgzrun
import asyncio

#===============================================================================================================
# Your Pure Pygame ZERO code

WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    screen.draw.text("Welcome to Pygame Zero", (100, 100), fontname="lemon days", fontsize=40, color=(255,215,0))
    screen.draw.text("Justin!", (630, 110), fontname="skincake", fontsize=40, color=(255,0,0))

#===============================================================================================================
# Pygbag Background Execution Loop

async def main():
    pgzrun.go()

    while True:
        # Hands thread priority back to the Chrome/Android engine
        await asyncio.sleep(0)

# Fire the script loop
asyncio.run(main())
