import pygame
import pgzero
import pgzrun
import asyncio

#===============================================================================================================
# Pygame ZERO code

WIDTH = 800
HEIGHT = 600


def draw():
    screen.clear()

    screen.draw.text("Welcome to Pygame Zero",(100, 100),fontname="lemon days",fontsize=40,color=(255,215,0))
    screen.draw.text("Justin!",(630, 110),fontname="skincake",fontsize=40,color=(255,0,0))

#===============================================================================================================
# Requirement for Pygbag running in a Browser

async def main():
    pgzrun.go()

    while True:
        try:
            update()
        except NameError:
            pass

        draw()
        pygame.display.flip()

        # Hands control back to Chrome/Android so it doesn't freeze gray
        await asyncio.sleep(0)

# Boot the script
asyncio.run(main())


