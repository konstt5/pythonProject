
import pygame

pygame.init()

import spg
from spg.core import *

screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)

clock = pygame.time.Clock()

running = True

desktop = spg.core.Desktop()

# *** TESTING HERE ***
artpath = "art/"

background = pygame.image.load(artpath + "back.jpg").convert()
#COMMON STYLES

# graphicButtonStyle = spg.styles.defaultButtonStyle

ok_icon = pygame.image.load(artpath + "ok.png").convert_alpha()
cancel_icon = pygame.image.load(artpath + "cancel.png").convert_alpha()

closeButtonSkin  = pygame.image.load(artpath + "close.png").convert_alpha()
shadeButtonSkin =  pygame.image.load(artpath + "shade.png").convert_alpha()

winStyle = {'font': spg.styles.titleFont,
              'font-color': (255,255,255),
              'offset-top-left': (14, 35),
              'offset-bottom-right': (14,14),
              'title-position': (10,10),
              
              'appearence': spg.styles.GRAPHICAL,
              
              'border-offset-top-left': (5,5),
              'border-offset-bottom-right': (7,5),
              
              'image-top-left': pygame.image.load(artpath + "win_topleft.png").convert_alpha(),
              'image-top': pygame.image.load(artpath + "win_top.png").convert_alpha(),
              'image-top-right': pygame.image.load(artpath + "win_topright.png").convert_alpha(),
              'image-right': pygame.image.load(artpath + "win_right.png").convert_alpha(),
              'image-bottom-right': pygame.image.load(artpath + "win_bottomright.png").convert_alpha(),
              'image-bottom': pygame.image.load(artpath + "win_bottom.png").convert_alpha(),
              'image-bottom-left': pygame.image.load(artpath + "win_bottomleft.png").convert_alpha(),
              'image-left': pygame.image.load(artpath + "win_left.png").convert_alpha(),
              'image-middle': pygame.image.load(artpath + "win_middle.png").convert_alpha(),
              
              'close-button-skin':  closeButtonSkin,
              'shade-button-skin': shadeButtonSkin,
              
              'close-button-offset': (10,7),
              'shade-button-offset': (32,7),
              'shade-button-only-offset': (10,7)
              }

# winStyle = spg.styles.defaultWindowStyle

checkBoxStyle = spg.styles.darkCheckBoxStyle

darkTheme = spg.styles.darkTheme
winTheme = spg.styles.winTheme
mainTheme = darkTheme

def show_dialog(widget):
    win = Window(parent = desktop, size = (300,140),mode = MODE_DIALOG, style = winStyle, title = "Dialog Window :P", shadeable = False, closeable = False)
    
    Label(parent = win, anchor = ANCHOR_TOP | ANCHOR_LEFT | ANCHOR_RIGHT, autosize = AUTOSIZE_VERTICAL_ONLY, text = "This is a Dialog Window. While there's one or more pending dialog windows, only the last one gets the input while the others are frozen until the last Dialog Window is closed.")
    
    Button(parent = win, position = (0,0), text = "OK", anchor =  ANCHOR_BOTTOM | ANCHOR_RIGHT,  theme=winTheme, image = ok_icon).connect('onClick', lambda widget: win.destroy())
    Button(parent = win, position = (60,0), text = "Open Another One!", theme=winTheme, anchor =  ANCHOR_BOTTOM | ANCHOR_RIGHT).connect('onClick', show_dialog)

win1 = Window(position = (100,120), title = "Window Always On Back", size = (320,120), parent = desktop, style = winStyle, mode = MODE_ALWAYS_BACK, closeable = False)
win1.shade()

Label(text = "This window will always be behind all the others. And this is very easy to do, just set the mode window property to MODE_ALWAYS_BACK while creating it.",
      parent = win1, size = (300,70), autosize = 0)

win2 =  Window( title = "Graphic Window", size = (440,300), parent = desktop, style = winStyle, resizable = True)
win2.min_size = (360,210)


Button(parent = win2, text = "OK", anchor =  ANCHOR_BOTTOM | ANCHOR_RIGHT,  theme=winTheme, image = ok_icon)
Button(parent = win2, text = "Cancel", position = (50,0), anchor =  ANCHOR_BOTTOM | ANCHOR_RIGHT,  theme=winTheme,  image = cancel_icon)
Button(parent = win2, position = 10, anchor = ANCHOR_BOTTOM| ANCHOR_LEFT | ANCHOR_RIGHT, theme=winTheme, text = "Open a Dialog Window", autosize =  0).connect('onClick', show_dialog)

Label(position = (0,0), text = "Welcome to Simple-Pygame-GUI 2! This is a very first version of the definitive game-focused GUI system for pygame. This is a basic demonstration of the new Window widget with its new features such as skinning, resizing, front windows, back windows, dialog windows, and so on. Hope you'll enjoy and please stay tuned for further updates and demos on http://www.keebus.net.",
      parent = win2, anchor = ANCHOR_TOP | ANCHOR_LEFT | ANCHOR_RIGHT, autosize  = AUTOSIZE_VERTICAL_ONLY)

CheckBox(text = "Check me! ;)", parent = desktop, position = (5, 5), theme=mainTheme, value=True, enabled=True)
Label(parent=desktop, position=(5, 25), text = "text label", theme=mainTheme, autosize=True)
TextBox(parent=desktop, position=(5, 45), size=(300, 20), anchor=ANCHOR_TOP | ANCHOR_LEFT,theme=mainTheme, text="text tststt sdjfldfkj aldkf jalajdflka jdsflkaj sdlfkja")
Button(parent=desktop, size=(100, 20), text="Cancel", position=(5, 70), theme=mainTheme)
ScrollBox(parent=desktop, position=(5, 95), size=(300, 20), anchor=ANCHOR_TOP | ANCHOR_LEFT,theme=mainTheme, value=0)

# *** END TESTING AREA ***

pygame.display.set_caption("Simple-Pygame-GUI Ver " + spg.__version__)

while running:
    tick = clock.tick(60)
    pygame.display.set_caption("%d" % clock.get_fps())
    for e in spg.setEvents():
        if e.type == pygame.QUIT:
            running = 0
        
        if e.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(e.size, pygame.RESIZABLE)
        
    screen.fill(spg.styles.darkTheme['BGColor'])
    
    # screen.blit(background, (0,0))
    
    desktop.update()
    
    desktop.draw()
    
    pygame.display.update()
    
pygame.quit()