import pygame
import pgzero
import pgzrun
import asyncio

#===============================================================================================================
# Pygame ZERO setup

WIDTH = 800
HEIGHT = 600

# 1. Initialize Pygame font module immediately
pygame.font.init()

# 2. Define the exact system font setups (or paths if files are present)
# Pygbag defaults perfectly to standard web fonts when given direct paths or None
try:
    # If font files exist in /fonts folder
    font_lemon = pygame.font.Font("fonts/lemon days.ttf", 40)
    font_skin = pygame.font.Font("fonts/skincake.ttf", 40)
except:
    # Fail-safe backup so the text renders regardless
    font_lemon = pygame.font.Font(None, 40)
    font_skin = pygame.font.Font(None, 40)

def draw():
    # Force a dark canvas clear over the default light grey browser box
    screen.fill((40, 40, 40))

    # 3. Render and blend text directly onto the display surface
    text_surface1 = font_lemon.render("Welcome to Pygame Zero", True, (255, 215, 0))
    text_surface2 = font_skin.render("Justin!", True, (255, 0, 0))
    
    # Blit (draw) the rendered text surfaces to the canvas positions
    screen.surface.blit(text_surface1, (100, 100))
    screen.surface.blit(text_surface2, (630, 110))

#===============================================================================================================
# Requirement for Pygbag running in a Browser

async def main():
    pgzrun.go()

    while True:
        try:
            pygame.event.pump()
        except:
            pass

        try:
            update()
        except NameError:
            pass

        draw()
        
        # 4. Refresh display frame
        pygame.display.update()

        # Hands control back to Chrome/Android so it doesn't freeze gray
        await asyncio.sleep(0)

# Boot the script
asyncio.run(main())

