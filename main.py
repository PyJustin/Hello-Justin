import pygame
import pgzero
import pgzrun
import asyncio

#===============================================================================================================
# Pygame ZERO code

WIDTH = 800
HEIGHT = 600

def draw():
    # Fill the screen surface so it draws over the default web layout grey background
    screen.fill((40, 40, 40)) 

    screen.draw.text("Welcome to Pygame Zero", (100, 100), fontname="lemon days", fontsize=40, color=(255,215,0))
    screen.draw.text("Justin!", (630, 110), fontname="skincake", fontsize=40, color=(255,0,0))

#===============================================================================================================
# Requirement for Pygbag running in a Browser

async def main():
    # 1. Initialize Pygame Zero properties
    pgzrun.go()

    while True:
        # 2. Let Pygame Zero process its internal events (required for screen text rendering)
        try:
            pygame.event.pump()
        except:
            pass

        try:
            update()
        except NameError:
            pass

        # 3. Call your text drawings
        draw()
        
        # 4. Use Pygbag's preferred browser refresh call instead of flip()
        pygame.display.update()

        # Hands control back to Chrome/Android so it doesn't freeze gray
        await asyncio.sleep(0)

# Boot the script
asyncio.run(main())

