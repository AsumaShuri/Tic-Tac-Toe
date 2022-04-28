#imports

import pygame, sys
import numpy as np

# inititating pygame
pygame.init()

# constants to easily change parameters such as background colour and size of panel
BLACK = (0,0,0)
CIRCLE_RAD = 30
CIRCLE_WIDTH= 5
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
font_display = 100
BG = (255,255,102)



#creating the console screen

screen =  pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT + font_display))
screen.fill(BG)
pygame.display.set_caption("TIC TAC TOE")
font = pygame.font.Font(pygame.font.get_default_font(), 11)
font2 = pygame.font.Font(pygame.font.get_default_font(), 25)

# CREATING ARRAY BOARD
board= np.zeros((3,3))


                                #FUNCTIONS  

# function to mark square
def mark_square(row,col,player):
    board[row][col]= player

# check if square is available
def available_square(row,col):
    return board[row][col] == 0

#check if board is full
def is_table_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

# function to mark circle or cross on the board
def draw_fig():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.circle(screen,BLACK,(int(col*100 + 50), int(row*100 +50)), CIRCLE_RAD, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line( screen, BLACK, (col * 100 + 27, row * 100 + 100 - 27), (col * 100 + 100 - 27, row * 100 + 27), 7 )
                pygame.draw.line( screen, BLACK, (col * 100 + 27, row * 100 + 27), (col * 100 + 100 - 27, row * 100 + 100 - 27), 7 )



# draw winning line-  veritcal, horizontal or diagonal 
def draw_win_vertical(col):
    posx = col* 100 + 100//2
    pygame.draw.line(screen,BLACK,(posx,0),(posx,300),5)

def draw_win_horizontal(row):
    posy = row* 100 +50
    pygame.draw.line(screen,BLACK,(0,posy),(300,posy),5)

def draw_win_asc():
    pygame.draw.line(screen, BLACK,(0,300),(300,0),5)

def draw_win_des():
    pygame.draw.line(screen, BLACK,(0,0),(300,300),5)

               
# condition for winning 
def win_check(player):

    #vertical check 
    for col in range(3):
        if board[0,col] == player and board[1,col] == player and board[2,col] == player:
            draw_win_vertical(col)
            return True

    #horizontal check 
    for row in range(3):
        if board[row,0] == player and board[row,1] == player and board[row,2] == player:
            draw_win_horizontal(row)
            return True
    
    # primary diagonal win check
    if board[0,0] == player and board[1,1] == player and board[2,2] == player:
        draw_win_des()
        return True

    # asc diagonal win check
    if board[2,0] == player and board[1,1] == player and board[0,2] == player:
        draw_win_asc()
        return True
    
    return False


# restart
def restart():
	screen.fill((255,255,102))
	draw_lines()
	for row in range(3):
		for col in range(3):
			board[row][col] = 0
       

#creating lines
def draw_lines():
    #vertical lines
    pygame.draw.line(screen, BLACK, (100,0),(100,300), 5)
    pygame.draw.line(screen, BLACK, (200,0),(200,300), 5)
    #horizontal
    pygame.draw.line(screen, BLACK, (0,100),(300,100), 5)
    pygame.draw.line(screen, BLACK, (0,200 ),(300,200), 5)
    pygame.draw.line(screen, BLACK, (0,300 ),(300,300), 5)
    pygame.draw.line(screen, BLACK, (0,350),(300,350), 5)

    # game box
    pygame.draw.line(screen, (0,0,0), (0,325),(300,325),50)
    pygame.draw.line(screen, (0,0,0), (0,375),(300,375),50)


# displaying text on board
def display_text():
    text_surface = font.render('PRESS r TO RESTART \n PRESS q TO QUIT', True, (255,255,255))
    screen.blit(text_surface, dest=(40,375))





#calling functions

draw_lines()
display_text()



#initalizing player for mark function as 1 and status of the game [over or ongoing]
player = 1
game_over = False



#main loop 

if __name__ == '__main__':
    while True:
    
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                sys.exit()


            if not game_over:
            
                new_text = font2.render( "PLAYER" + str(player) + '\'s Turn!', True, (255,255,255))
                screen.blit(new_text, dest=(50,325))
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                
                mouseX= event.pos[0]
                mouseY= event.pos[1]

                X= int(mouseY//100)
                Y= int(mouseX//100)

                try:
                
                    if available_square(X,Y):
                    
                    
                        mark_square(X,Y,player)
                                
                        print(board)

                        #to overwrite previous text so they dont stack
                        pygame.draw.line(screen, (0,0,0), (0,325),(300,325),50)

                        if win_check(player):
                            print(str(player) + "wins!")
                                    
                            win_text = font2.render( "PLAYER" + str(player) +  ' WINS! ', True, (255,255,255))
                            screen.blit(win_text, dest=(50,325))

                                    
                            game_over =True

                        if is_table_full() and not game_over:
                        
                            print('table is full!')
                            pygame.draw.line(screen, (0,0,0), (0,325),(300,325),50)
                            draw_text = font2.render( "---DRAW---!", True, (255,255,255))
                            screen.blit(draw_text, dest=(70,325))
                            game_over = True
                                
                            
                        player= player % 2 + 1

                        draw_fig()

                        

                            
                except IndexError:
                
                    continue
                              
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    print('restarting...')
                    player = 1
                    game_over = False
                    display_text()
                if event.key == pygame.K_q:
                
                    sys.exit("Thank you for playing!")
                    
        
        
        
            pygame.display.update()  

       