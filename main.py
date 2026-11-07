#!pgzrun
#===============================================================================================================
# Pure Pygame ZERO Code (Pygbag Natively Detects the Shebang Above!)

WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    
    # Note: Keep the folder named exactly "fonts" in lowercase.
    # The font names inside the files must be written in lowercase here if they aren't loading.
    screen.draw.text("Welcome to Pygame Zero", (100, 100), fontname="lemon days", fontsize=40, color=(255,215,0))
    screen.draw.text("Justin!", (630, 110), fontname="skincake", fontsize=40, color=(255,0,0))
