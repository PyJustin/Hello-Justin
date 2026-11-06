# /// script
# dependencies = [
#   "pgzero",
#   "timeit"
# ]
# ///
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
        # Crucial web handle: hands thread priority back to the Chrome/Android engine
        await asyncio.sleep(0)

# Fire the script loop
asyncio.run(main())
