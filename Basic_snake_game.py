import pygame
import random

pygame.init()

# color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

# create window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My First Game")
pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):

    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):

    for x,y in snk_list:

        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# welcome function
def welcome():

    exit_game = False
    while not exit_game:

        gameWindow.fill(white)
        text_screen("Welcome To Game", black, 250,200)
        text_screen("Press Any Key...", black, 280,250)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                game_loop()

        pygame.display.update()
        clock.tick(45)

# creating a game loop
def game_loop():

    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 40
    velocity_x = 0
    velocity_y = 0
    speed = 5

    food_x = random.randint(40, screen_width-35)
    food_y = random.randint(40, screen_height-35)

    score = 0
    snake_size = 20
    fps = 60

    key_right = False
    key_left = False
    key_up = False
    key_down = False

    with open("D:\Visual Studio Code\pyGame\high_score.txt","r") as file:

        high_score = file.read()
    
    snake_list = []

    snake_length = 1

    while not exit_game:

        if game_over:

            with open("D:\Visual Studio Code\pyGame\high_score.txt","w") as file:

                file.write(str(high_score))
                
            gameWindow.fill(red)

            text_screen("Game Over! Press Enter", white, 210, 200)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:

                        game_loop()

        else:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT and not key_left:

                        velocity_x = speed
                        velocity_y = 0
                        key_right = True
                        key_left = False
                        key_up = False
                        key_down = False
                    
                    if event.key == pygame.K_LEFT and not key_right:

                        velocity_x = -speed
                        velocity_y = 0
                        key_right = False
                        key_left = True
                        key_up = False
                        key_down = False

                    if event.key == pygame.K_UP and not key_down:

                        velocity_y = -speed
                        velocity_x = 0
                        key_right = False
                        key_left = False
                        key_up = True
                        key_down = False

                    if event.key == pygame.K_DOWN and not key_up:
                        
                        velocity_y = speed
                        velocity_x = 0
                        key_right = False
                        key_left = False
                        key_up = False
                        key_down = True
            
            snake_x += velocity_x
            snake_y += velocity_y   
            
            # food is eaten when difference of any exis is less then snake_size.
            # also snake_size == food_size

            if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
                score += 3
                food_x = random.randint(40, screen_width-35)
                food_y = random.randint(40, screen_height-35)

                snake_length += 4

                if score > int(high_score):

                    high_score = score

            gameWindow.fill(white)
            text_screen("Score: " + str(score) + "    High Score: " + str(high_score), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            
            head = []

            head.append(snake_x)

            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:

                del snake_list[0]

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:

                game_over = True
            
            if head in snake_list[:-1]:

                game_over = True

            plot_snake(gameWindow, black, snake_list, snake_size)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()

# start function
welcome()