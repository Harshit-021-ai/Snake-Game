import pygame
import random
pygame.init()

# Colours
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
White = (255, 255, 255)

Screen_Width = 900
Screen_Height = 600
# Creating Window
Game_Window = pygame.display.set_mode((Screen_Width, Screen_Height))

# Game Title
pygame.display.set_caption("Snake Game By Harshit Sharma")
pygame.display.update()

# Game specific variables
Game_Exit = False
Game_Over = False
Snake_x = 45
Snake_y = 55
Velocity_x = 0
Velocity_y = 0
Snake_Size = 20
fps = 30
Score = 0
Food_x = random.randint(20, Screen_Width//2)
Food_y = random.randint(20, Screen_Height//2)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_Screen(text, color, x, y):
    Screen_Text = font.render(text, True, color)
    Game_Window.blit(Screen_Text, [x, y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

snk_list = []
snk_length = 1

# Game Loop
while not Game_Exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Velocity_x = 5
                Velocity_y = 0

            if event.key == pygame.K_LEFT:
                Velocity_x = -5
                Velocity_y = 0

            if event.key == pygame.K_UP:
                Velocity_y = -5
                Velocity_x = 0

            if event.key == pygame.K_DOWN:
                Velocity_y = 5
                Velocity_x = 0

    Snake_x = Snake_x + Velocity_x
    Snake_y = Snake_y + Velocity_y

    if abs(Snake_x - Food_x) < 15 and abs(Snake_y - Food_y) < 15:
        Score += 1
        Food_x = random.randint(20, (Screen_Width//2))
        Food_y = random.randint(20, (Screen_Height//2))
        snk_length += 5

    Game_Window.fill(White)
    text_Screen("Score: " + str(Score), Black, 5, 5)
    pygame.draw.rect(Game_Window, Red, [Food_x, Food_y, Snake_Size, Snake_Size])

    head = []
    head.append(Snake_x)
    head.append(Snake_y)
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    plot_snake(Game_Window, Black, snk_list, Snake_Size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
