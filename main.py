# /// script
# dependencies = [
#   "pgzero"
# ]
# ///
import sys
import types
import pygame

# 1. FIX THE WINDOW ICON RESOURCING CRASH
pygame.font.init()
if not pygame.display.get_init():
    pygame.display.init()
fake_icon = pygame.Surface((32, 32))
pygame.display.set_icon = lambda icon_surface: None

# 2. EMULATE THE THREADING ENGINE FOR PYTHON 3.12 COMPATIBILITY
class SafeThread:
    def __init__(self, *args, **kwargs): pass
    def setDaemon(self, val): pass
    def start(self): pass

if 'threading' not in sys.modules:
    fake_threading = types.ModuleType('threading')
    fake_threading.Thread = SafeThread
    sys.modules['threading'] = fake_threading

# 3. EMULATE TIMEIT FOR THE INTERNAL GAME ENGINE CLOCK
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
    
    # NOTE: Ensure "lemon days.ttf" and "skincake.ttf" exist inside a "fonts" folder in your repository!
    # If you don't have them yet, remove 'fontname="..."' to use the default system font for testing.
    screen.draw.text("Welcome to Pygame Zero", (100, 100), fontname="lemon days", fontsize=40, color=(255,215,0))
    screen.draw.text("Justin!", (630, 110), fontname="skincake", fontsize=40, color=(255,0,0))

#===============================================================================================================
# Pygbag Background Execution Loop

async def main():
    # Initialize the Pygame Zero runner engine without launching the blocking desktop loop
    pgzrun.init() 

    while True:
        # Manually tick the Pygame Zero engine frame by frame
        pgzrun.core.ptext.memory.clear() # Clear frame text cache
        pgzrun.core.get_runner().frame_loop() 
        
        # Hands thread priority back to the browser engine to draw the screen
        await asyncio.sleep(0)

# Fire the script loop
asyncio.run(main())


async def main():
    pgzrun.go()

    while True:
        # Hands thread priority back to the Chrome/Android engine
        await asyncio.sleep(0)

# Fire the script loop
asyncio.run(main())
