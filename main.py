#!pgzrun
#===============================================================================================================
# Pure Pygame ZERO Code 

WIDTH = 800
HEIGHT = 600

def draw():
    # 1. FIX: Replace screen.clear() with screen.fill() to establish a solid canvas layer
    screen.fill((40, 40, 40)) # A clean dark grey background
    
    # 2. Draw your styled text over the solid layer
    screen.draw.text("Welcome to Pygame Zero", (100, 100), fontname="lemon days", fontsize=40, color=(255,215,0))
    screen.draw.text("Justin!", (630, 110), fontname="skincake", fontsize=40, color=(255,0,0))

def update():
    # Pygbag looks for this update function to cycle the frame engine properly
    pass
