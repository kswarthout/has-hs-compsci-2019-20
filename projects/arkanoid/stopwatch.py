"""
 Show how to put a timer on the screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_RED = (255, 0, 0)

counter = -1
running = False
time_elapsed = 0
display = 'Welcome!'


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font(None, 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def start():
    global running
    global time_elapsed
    running = True
    time_elapsed = 0


def stop():
    global running
    running = False


pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Timer")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# font for stopwatch
timer_text = pygame.font.Font(None, 40)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)

    # Stopwatch Buttons
    button("Start", 100, 350, 100, 50, GREEN, BRIGHT_GREEN, start)
    button("Stop", 500, 350, 100, 50, RED, BRIGHT_RED, stop)

    textSurf, textRect = text_objects(display, timer_text)
    textRect.center = (250, 250)
    screen.blit(textSurf, textRect)

    time_elapsed += clock.tick()
    if running:
        if time_elapsed > 1000:
            counter += 1
            time_elapsed = 0
        if counter == -1:
            display = 'Starting...'
        else:
            display = str(counter)

    elif counter == -1:
        display = 'Welcome!'

    textSurf, textRect = text_objects(display, timer_text)
    textRect.center = (250, 250)
    screen.blit(textSurf, textRect)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
