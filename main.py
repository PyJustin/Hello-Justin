# /// script
# dependencies = [
#   "pgzero"
# ]
# ///
import sys
import types
import threading

# 1. PYTHON 3.12 COMPATIBILITY PATCH FOR PYGAME ZERO TONE GENERATOR
# Fixes 'Thread' object has no attribute 'setDaemon' crash
threading.Thread.setDaemon = lambda self, daemonic: setattr(self, 'daemon', daemonic)

# 2. FAKE TIMEIT MODULE: Satisfies the internal web loops instantly
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
