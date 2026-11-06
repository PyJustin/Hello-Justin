#!pgzrun       # must be 1st line
import pgzrun

WIDTH = 800
HEIGHT = 600


#=========================================================================================================================
# MAINLINE (Calls to Functions)
#=========================================================================================================================

def draw():
    draw_hello()

#=========================================================================================================================
# FUNCTION Definitions (sub-routines)
#=========================================================================================================================

def draw_hello():
    screen.draw.text("Welcome to Pygame ZERO ", center=(WIDTH // 2, HEIGHT // 2 - 30), fontname="lemon days", fontsize=32, color=(255, 255, 0))
    screen.draw.text(" Justin ! ", center=(WIDTH // 2, HEIGHT // 2 + 30), fontname="skincake", fontsize=32, color=(255, 0, 0))


pgzrun.go()  # must be the last line to run in Pyscrypter ; but comment-out this line to build a PWA (no other changes required for a PWA).


