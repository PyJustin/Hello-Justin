import pygame
import pgzero
import pgzrun
import asyncio

#===============================================================================================================
# Pygame ZERO code

WIDTH = 800
HEIGHT = 600

def draw():
    # Clear the screen container explicitly with a color block
    screen.fill((40, 40, 40))

    # Render your custom font texts
    screen.draw.text("Welcome to Pygame Zero", (100, 100), fontname="lemon days", fontsize=40, color=(255,215,0))
    screen.draw.text("Justin!", (630, 110), fontname="skincake", fontsize=40, color=(255,0,0))

#===============================================================================================================
# Requirement for Pygbag running in a Browser

async def main():
    # 1. Mount the Pygame Zero variables globally into the local scope
    global screen, keyboard, images, sounds

    # 2. Boot the engine wrapper properties
    pgzrun.go()

    while True:
        # 3. Pull events to clear Chrome's canvas rendering restriction
        pygame.event.pump()

        try:
            update()
        except NameError:
            pass

        # 4. Trigger drawing frames
        draw()
        
        # 5. Flush the visual layout to the web container
        pygame.display.flip()

        # 6. Relinquish processing control so Chrome/Android doesn't freeze gray
        await asyncio.sleep(0)

# Execute the application
asyncio.run(main())

