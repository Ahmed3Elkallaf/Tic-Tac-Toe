import pygame

screen = pygame.display.set_mode((600,400))

# draw some hidden squares
box1 = pygame.draw.rect(screen,(0,0,0),(80,30,130,100))
box2 = pygame.draw.rect(screen,(0,0,0),(245,30,130,100))
box3 = pygame.draw.rect(screen,(0,0,0),(400,30,130,100))
box4 = pygame.draw.rect(screen,(0,0,0),(75,155,140,100))
box5 = pygame.draw.rect(screen,(0,0,0),(245,155,130,100))
box6 = pygame.draw.rect(screen,(0,0,0),(405,155,130,100))
box7 = pygame.draw.rect(screen,(0,0,0),(85,280,130,100))
box8 = pygame.draw.rect(screen,(0,0,0),(245,280,130,100))
box9 = pygame.draw.rect(screen,(0,0,0),(405,280,130,100))


# displaying images
board = pygame.transform.scale(pygame.image.load("Tic-Tac-Toe-Board.jpg"),(600,400))
screen.blit(board,(0,0))

X = pygame.transform.scale(pygame.image.load("X.png"),(80,80))

O = pygame.transform.scale(pygame.image.load("O.png"),(80,80))

WIN_X = pygame.transform.scale(pygame.image.load("red_X.jpg"),(80,80))

WIN_O = pygame.transform.scale(pygame.image.load("green_O.jpg"),(80,80))


rest_img = pygame.transform.scale(pygame.image.load("rest button.jpg"),(60,60))
rest_button = rest_img.get_rect()
screen.blit(rest_img,(rest_button))

# variables
x = True

bol_box1X = False
bol_box2X = False
bol_box3X = False
bol_box4X = False
bol_box5X = False
bol_box6X = False
bol_box7X = False
bol_box8X = False
bol_box9X = False


bol_box1O = False
bol_box2O = False
bol_box3O = False
bol_box4O = False
bol_box5O = False
bol_box6O = False
bol_box7O = False
bol_box8O = False
bol_box9O = False



run = True


# game

while run:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and box1.collidepoint(mouse) and x:
            screen.blit(X,(110,50))
            x = False
            box1.x = 900
            bol_box1X = True
        
        elif event.type == pygame.MOUSEBUTTONDOWN and box1.collidepoint(mouse) and not x:
            screen.blit(O,(110,50))
            x = True
            box1.x = 900
            bol_box1O = True


        if event.type == pygame.MOUSEBUTTONDOWN and box2.collidepoint(mouse) and x:
            screen.blit(X,(280,50))
            x = False
            box2.x = 900
            bol_box2X = True

        elif event.type == pygame.MOUSEBUTTONDOWN and box2.collidepoint(mouse) and not x:
            screen.blit(O,(280,50))
            x = True
            box2.x = 900
            bol_box2O = True


        if event.type == pygame.MOUSEBUTTONDOWN and box3.collidepoint(mouse) and x:
            screen.blit(X,(450,50))
            x = False
            box3.x = 900
            bol_box3X = True

        elif event.type == pygame.MOUSEBUTTONDOWN and box3.collidepoint(mouse) and not x:
            screen.blit(O,(450,50))
            x = True
            box3.x = 900
            bol_box3O = True



        if event.type == pygame.MOUSEBUTTONDOWN and box4.collidepoint(mouse) and x:
            screen.blit(X,(120,170))
            x = False
            box4.x = 900
            bol_box4X = True


        elif event.type == pygame.MOUSEBUTTONDOWN and box4.collidepoint(mouse) and not x:
            screen.blit(O,(120,170))
            x = True
            box4.x = 900
            bol_box4O = True



        if event.type == pygame.MOUSEBUTTONDOWN and box5.collidepoint(mouse) and x:
            screen.blit(X,(280,170))
            x = False
            box5.x = 900
            bol_box5X = True


        elif event.type == pygame.MOUSEBUTTONDOWN and box5.collidepoint(mouse) and not x:
            screen.blit(O,(280,170))
            x = True
            box5.x = 900
            bol_box5O = True

            
        if event.type == pygame.MOUSEBUTTONDOWN and box6.collidepoint(mouse) and x:
            screen.blit(X,(450,170))
            x = False
            box6.x = 900
            bol_box6X = True

        elif event.type == pygame.MOUSEBUTTONDOWN and box6.collidepoint(mouse) and not x:
            screen.blit(O,(450,170))
            x = True
            box6.x = 900
            bol_box6O = True


        if event.type == pygame.MOUSEBUTTONDOWN and box7.collidepoint(mouse) and x:
            screen.blit(X,(110,300))
            x = False
            box7.x = 900
            bol_box7X = True


        elif event.type == pygame.MOUSEBUTTONDOWN and box7.collidepoint(mouse) and not x:
            screen.blit(O,(110,300))
            x = True
            box7.x = 900
            bol_box7O = True


        if event.type == pygame.MOUSEBUTTONDOWN and box8.collidepoint(mouse) and x:
            screen.blit(X,(280,300))
            x = False
            box8.x = 900
            bol_box8X = True


        elif event.type == pygame.MOUSEBUTTONDOWN and box8.collidepoint(mouse) and not x:
            screen.blit(O,(280,300))
            x = True
            box8.x = 900
            bol_box8O = True


        if event.type == pygame.MOUSEBUTTONDOWN and box9.collidepoint(mouse) and x:
            screen.blit(X,(450,300))
            x = False
            box9.x = 900
            bol_box9X = True


        elif event.type == pygame.MOUSEBUTTONDOWN and box9.collidepoint(mouse) and not x:
            screen.blit(O,(450,300))
            x = True
            box9.x = 900
            bol_box9O = True


        # X win
        if bol_box1X and bol_box2X and bol_box3X:
            screen.blit(WIN_X,(110,50))
            screen.blit(WIN_X,(280,50))
            screen.blit(WIN_X,(450,50))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box4X and bol_box5X and bol_box6X:
            screen.blit(WIN_X,(120,170))
            screen.blit(WIN_X,(280,170))
            screen.blit(WIN_X,(450,170))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box7X and bol_box8X and bol_box9X:
            screen.blit(WIN_X,(110,300))
            screen.blit(WIN_X,(280,300))
            screen.blit(WIN_X,(450,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box1X and bol_box4X and bol_box7X:
            screen.blit(WIN_X,(110,50))
            screen.blit(WIN_X,(120,170))
            screen.blit(WIN_X,(110,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box2X and bol_box5X and bol_box8X:
            screen.blit(WIN_X,(280,50))
            screen.blit(WIN_X,(280,170))
            screen.blit(WIN_X,(280,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box3X and bol_box6X and bol_box9X:
            screen.blit(WIN_X,(450,50))
            screen.blit(WIN_X,(450,170))
            screen.blit(WIN_X,(450,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box1X and bol_box5X and bol_box9X:
            screen.blit(WIN_X,(110,50))
            screen.blit(WIN_X,(280,170))
            screen.blit(WIN_X,(450,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box3X and bol_box5X and bol_box7X:
            screen.blit(WIN_X,(450,50))
            screen.blit(WIN_X,(280,170))
            screen.blit(WIN_X,(110,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        
        # O win
        if bol_box1O and bol_box2O and bol_box3O:
            screen.blit(WIN_O,(110,50))
            screen.blit(WIN_O,(280,50))
            screen.blit(WIN_O,(450,50))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box4O and bol_box5O and bol_box6O:
            screen.blit(WIN_O,(120,170))
            screen.blit(WIN_O,(280,170))
            screen.blit(WIN_O,(450,170))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box7O and bol_box8O and bol_box9O:
            screen.blit(WIN_O,(110,300))
            screen.blit(WIN_O,(280,300))
            screen.blit(WIN_O,(450,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box1O and bol_box4O and bol_box7O:
            screen.blit(WIN_O,(110,50))
            screen.blit(WIN_O,(120,170))
            screen.blit(WIN_O,(110,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box2O and bol_box5O and bol_box8O:
            screen.blit(WIN_O,(280,50))
            screen.blit(WIN_O,(280,170))
            screen.blit(WIN_O,(280,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box3O and bol_box6O and bol_box9O:
            screen.blit(WIN_O,(450,50))
            screen.blit(WIN_O,(450,170))
            screen.blit(WIN_O,(450,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box1O and bol_box5O and bol_box9O:
            screen.blit(WIN_O,(110,50))
            screen.blit(WIN_O,(280,170))
            screen.blit(WIN_O,(450,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900

        if bol_box3O and bol_box5O and bol_box7O:
            screen.blit(WIN_O,(450,50))
            screen.blit(WIN_O,(280,170))
            screen.blit(WIN_O,(110,300))
            box1.x = 900
            box2.x = 900
            box3.x = 900
            box4.x = 900
            box5.x = 900
            box6.x = 900
            box7.x = 900
            box8.x = 900
            box9.x = 900


        # rest button function
        if event.type == pygame.MOUSEBUTTONDOWN and rest_button.collidepoint(mouse):
            x = True
            bol_box1X = False
            bol_box2X = False
            bol_box3X = False
            bol_box4X = False
            bol_box5X = False
            bol_box6X = False
            bol_box7X = False
            bol_box8X = False
            bol_box9X = False
            bol_box1O = False
            bol_box2O = False
            bol_box3O = False
            bol_box4O = False
            bol_box5O = False
            bol_box6O = False
            bol_box7O = False
            bol_box8O = False
            bol_box9O = False
            box1 = pygame.draw.rect(screen,(0,0,0),(80,30,130,100))
            box2 = pygame.draw.rect(screen,(0,0,0),(245,30,130,100))
            box3 = pygame.draw.rect(screen,(0,0,0),(400,30,130,100))
            box4 = pygame.draw.rect(screen,(0,0,0),(75,155,140,100))
            box5 = pygame.draw.rect(screen,(0,0,0),(245,155,130,100))
            box6 = pygame.draw.rect(screen,(0,0,0),(405,155,130,100))
            box7 = pygame.draw.rect(screen,(0,0,0),(85,280,130,100))
            box8 = pygame.draw.rect(screen,(0,0,0),(245,280,130,100))
            box9 = pygame.draw.rect(screen,(0,0,0),(405,280,130,100))

            screen.blit(board,(0,0))
            screen.blit(rest_img,(rest_button))


    pygame.display.update()


pygame.quit()