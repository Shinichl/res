import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

# Load button images
resume_img = pygame.image.load("Menu/images/button_resume.png").convert_alpha()
options_img = pygame.image.load("Menu/images/button_options.png").convert_alpha()
quit_img = pygame.image.load("Menu/images/button_quit.png").convert_alpha()
OFFsound_img = pygame.image.load('Menu/images/button_OFFsound.png').convert_alpha()
ONsound_img = pygame.image.load('Menu/images/button_ONsound.png').convert_alpha()
back_img = pygame.image.load('Menu/images/button_back.png').convert_alpha()

# Create button instances
resume_button = button.Button(200, 125, resume_img, 1)
options_button = button.Button(195, 250, options_img, 1)
quit_button = button.Button(227, 375, quit_img, 1)
OFFsound_button = button.Button(125, 225, OFFsound_img, 1)
ONsound_button = button.Button(126, 75, ONsound_img, 1)
back_button = button.Button(205, 350, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      
      if ONsound_button.draw(screen):
        print("ON Sound")
      if OFFsound_button.draw(screen):
        print("OFF Sound")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()