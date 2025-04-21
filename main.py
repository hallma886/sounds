# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import random
import config  # Import the config module


def init_game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def draw_text(screen, text, text_font, text_color, y):
    text_font = pygame.font.SysFont("Arial", 30)
    inserted_text = text_font.render(text, True, text_color)
    screen.blit(inserted_text, (90, y))

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    
    base_y = 30

    line_height = 20
    text_font = pygame.font.Font(None, 30)
    
    instructions = ["Press 'a' to play Sound Effect #1", "Press 's' to play Sound Effect #2"]
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 

        for i in range(len(instructions)):
            draw_text(screen, instructions[i], text_font, config.BLACK, base_y + i * line_height)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                config.DOOM_SOUND_EFFECT.play()
            if keys[pygame.K_w]:
                config.ZAP.play()
            if keys[pygame.K_e]:
                config.BEEP.play()
            if keys[pygame.K_r]:
                config.ATOMIC_CAT.play()
            if keys[pygame.K_t]:
                config.LASER.play()
            if keys[pygame.K_a]:
                config.ROBLOX_DEATH_SOUND.play()
            







        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































