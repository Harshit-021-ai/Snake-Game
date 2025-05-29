import pygame
import random
import os
pygame.init()

# Colours
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
White = (255, 255, 255)

# Creating Window
Screen_Width = 900
Screen_Height = 600
Game_Window = pygame.display.set_mode((Screen_Width, Screen_Height))

# Game Title
pygame.display.set_caption("Snake Game By Harshit Sharma")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def Text_Screen(text, color, x, y):
    Screen_Text = font.render(text, True, color)
    Game_Window.blit(Screen_Text, [x, y])

def plot_snake(gamewindow, color, Snake_list, Snake_Size):
    for x, y in Snake_list:
        pygame.draw.rect(gamewindow, color, [x, y, Snake_Size, Snake_Size])

def Welcome():
    Exit_Game= False
    while not Exit_Game:
        Game_Window.fill((233,220,229))
        Text_Screen("Welcome To Snakes", Black, 260, 250)
        Text_Screen("Press Space Bar To Play", Black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit_Game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
    
        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables
    Game_Exit = False
    Game_Over = False
    Snake_x = 45
    Snake_y = 55
    Velocity_x = 0
    Velocity_y = 0
    Snake_list = []
    Snake_length = 1
    # Check if HighScore file exists
    if (not os.path.exists("HighScore.txt")):
        with open("HighScore.txt", "w") as f:
            f.write("0")
            
    with open("HighScore.txt", "r") as f:
        High_Score = f.read()

    Food_x = random.randint(0, Screen_Width)
    Food_y = random.randint(0, Screen_Height)
    Score = 0
    init_Velocity = 5
    Snake_Size = 20
    fps = 60
    while not Game_Exit:
        if Game_Over:
            with open("HighScore.txt", "w")as f:
                f.write(str(High_Score))
            Game_Window.fill((233,220,229))
            Text_Screen("Game Over! Press Enter to Continue", Red,110, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game_Exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()

        else:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game_Exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        Velocity_x = init_Velocity
                        Velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        Velocity_x = -init_Velocity
                        Velocity_y = 0

                    if event.key == pygame.K_UP:
                        Velocity_y = -init_Velocity
                        Velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        Velocity_y = init_Velocity
                        Velocity_x = 0

            Snake_x = Snake_x + Velocity_x
            Snake_y = Snake_y + Velocity_y

            if abs(Snake_x - Food_x) < 20 and abs(Snake_y - Food_y) < 20:
                Score += 1
                Food_x = random.randint(20, (Screen_Width//2))
                Food_y = random.randint(20, (Screen_Height//2))
                Snake_length += 5
                if Score>int (High_Score):
                    High_Score = Score
            
            Game_Window.fill(White)
            Text_Screen("Score: " + str(Score) + "  HighScore: "+str(High_Score), Red, 5, 5)
            pygame.draw.rect(Game_Window, Red, [Food_x, Food_y, Snake_Size, Snake_Size])

            head = []
            head.append(Snake_x)
            head.append(Snake_y)
            Snake_list.append(head)

            if len(Snake_list) > Snake_length:
                del Snake_list[0]

            if head in Snake_list[:-1]:
                Game_Over = True
            
            if Snake_x<0 or Snake_x>Screen_Width or Snake_y<0 or Snake_y>Screen_Height:
                Game_Over = True
            plot_snake(Game_Window, Black, Snake_list, Snake_Size)
        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()
    quit()
Welcome()
