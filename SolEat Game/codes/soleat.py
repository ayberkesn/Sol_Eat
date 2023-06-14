import pygame
import random
from Button import button
from healthBar import hp
#SolEat Game made by Alaettin Ayberk Esen
#You can play this game with W,A,S,D buttons or arrow keys
#Goal is collecting 25 coins with whale character 
#If you interact with bomb it will reduce your HP by 10 (Max HP is 100)
#If you collect 10 coins whale will get bigger,move slower and regain 20 HP
#For pausing the game please press SPACE button
#Have fun with the game!


pygame.init()

width,height = (600,750)
gameScreen = pygame.display.set_mode((width,height))

pygame.display.set_caption("SolEat")
gameIcon = pygame.image.load("whaleTail.png")
pygame.display.set_icon(gameIcon)

#setting the game sounds
pygame.mixer.music.load("water.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.75)

levelUpSound = pygame.mixer.Sound("levelUp.wav")
coinCollectSound = pygame.mixer.Sound("coinCollect.wav")

explosionSound = pygame.mixer.Sound("explosion.wav")

endSound = pygame.mixer.Sound("gameOverSound.wav")
winSound = pygame.mixer.Sound("winSound.wav")

#Setting the FPS
speed = 10
fps = 60
time = pygame.time.Clock()

#Loading the images of whale,coin and buttons
whale = pygame.image.load("whale.png")
whale_coor = whale.get_rect()
whale_coor.topleft = (width/2,height/2) 

coin = pygame.image.load("sol.png")
coin_coor = coin.get_rect()
coin_coor.topleft = (random.randint(0,width-32),random.randint(91,height-32))

bomb1 = pygame.image.load("bomb.png")
bomb2 = pygame.image.load("bomb.png")
bomb3 = pygame.image.load("bomb.png")
bomb4 = pygame.image.load("bomb.png")

bomb1_coor = bomb1.get_rect()
bomb2_coor = bomb2.get_rect()
bomb3_coor = bomb3.get_rect()
bomb4_coor = bomb1.get_rect()

bomb1_coor.topleft = (random.randint(0,width-32),random.randint(91,height-32))
bomb2_coor.topleft = (random.randint(0,width-32),random.randint(91,height-32))
bomb3_coor.topleft = (random.randint(0,width-32),random.randint(91,height-32))
bomb4_coor.topleft = (random.randint(0,width-32),random.randint(91,height-32))

loseIcon = pygame.image.load("lose.png")
loseIcon_coor = loseIcon.get_rect()
loseIcon_coor.center = (width/2,150)

winIcon = pygame.image.load("winner.png")
winIcon_coor = winIcon.get_rect()
winIcon_coor.center = (width/2,150)

gameBackground = pygame.image.load("space.png")

startImage = pygame.image.load("startButton.png")
quitImage = pygame.image.load("exit.png")
continueImage = pygame.image.load("continue.png").convert_alpha()




#creating buttons
startButton = button(width/2,height/2,startImage,1)
quitButton = button(width/2,(height/2)+100,quitImage,1)
continueButton = button(width/2,height/2,continueImage,1)


#Setting fonts
font = pygame.font.SysFont("gameoverregular",128)
titleFont = pygame.font.SysFont("gamepowerregular",128)
endFont = pygame.font.SysFont("palatinolinotype",64)
endFontMsg = pygame.font.SysFont("palatinolinotype",32)


winFont = pygame.font.SysFont("segoeprint",64)
winFontMsg = pygame.font.SysFont("segoeprint",32)

pauseFont = pygame.font.SysFont("gameplayed",64)

#stats
score = 0
health_bar = hp(335,35,250,40,100)


#changing vars
y = 0
p = 0
w = 0
gameStatus = "menu"

#Game executer
gameOn = True


while gameOn:
    
    gameScreen.blit(gameBackground,(0,0))
    title = titleFont.render("SolEat",True,(51,255,153))
    title_coor = title.get_rect()
    title_coor.center = (width/2,80)
    gameScreen.blit(title,title_coor)


    if startButton.draw(gameScreen) or gameStatus == "inGame":
        
        gameScreen.blit(gameBackground,(0,0))
        gameScreen.blit(coin,coin_coor)
        gameScreen.blit(whale,whale_coor)
        gameScreen.blit(bomb1,bomb1_coor)
        gameScreen.blit(bomb2,bomb2_coor)
        gameScreen.blit(bomb3,bomb3_coor)
        gameScreen.blit(bomb4,bomb4_coor)

        health_bar.draw(gameScreen)


        scoreBoard = font.render("Score: " + str(score),True,(204,255,255))
        scoreBoard_coor = scoreBoard.get_rect()
        scoreBoard_coor.topleft = (10,10)

        pygame.draw.line(gameScreen,(255,255,255),(0,90),(600,90),3)
        gameScreen.blit(scoreBoard,scoreBoard_coor)


        if (coin_coor == bomb1_coor) or (coin_coor == bomb2_coor) or (coin_coor == bomb3_coor) or (coin_coor == bomb4_coor):
            coin_coor.x = random.randint(0,width-32)
            coin_coor.y = random.randint(91,height-32)


        button = pygame.key.get_pressed()
        if (button[pygame.K_LEFT]  or button[pygame.K_a])and whale_coor.left > 0:
            whale_coor.x -= speed
        elif (button[pygame.K_RIGHT] or button[pygame.K_d]) and whale_coor.right < width:
            whale_coor.x += speed
        elif (button[pygame.K_UP] or button[pygame.K_w]) and whale_coor.top > 0:
            whale_coor.y -= speed
        elif (button[pygame.K_DOWN] or button[pygame.K_s]) and whale_coor.bottom < height:
            whale_coor.y += speed

        if (whale_coor.colliderect(bomb1_coor)):

            explosionSound.play()
            health_bar.hp -= 10

            bomb1_coor.x = random.randint(0,width-32)
            bomb1_coor.y = random.randint(91,height-32)

        
        if (whale_coor.colliderect(bomb2_coor)):

            explosionSound.play()
            health_bar.hp -= 10

            bomb2_coor.x = random.randint(0,width-32)
            bomb2_coor.y = random.randint(91,height-32)

        if (whale_coor.colliderect(bomb3_coor)):

            explosionSound.play()
            health_bar.hp -= 10

            bomb3_coor.x = random.randint(0,width-32)
            bomb3_coor.y = random.randint(91,height-32)

        if (whale_coor.colliderect(bomb4_coor)):

            explosionSound.play()
            health_bar.hp -= 10

            bomb4_coor.x = random.randint(0,width-32)
            bomb4_coor.y = random.randint(91,height-32)



        if whale_coor.colliderect(coin_coor):
            coinCollectSound.play()
            coin_coor.x = random.randint(0,width-32)
            coin_coor.y = random.randint(91,height-32)
            score += 1

        if (bomb1_coor.left > 0):
            bomb1_coor.x += 4

            if bomb1_coor.right > width:
                bomb1_coor.x = 1
                bomb1_coor.y = random.randint(91,height-32)

        if (bomb2_coor.right < width):
            bomb2_coor.x -= 4

            if bomb2_coor.left < 0:
                bomb2_coor.x = width-33
                bomb2_coor.y = random.randint(91,height-32)

        if (bomb3_coor.top > 91):
            bomb3_coor.y += 4

            if bomb3_coor.bottom > height:
                bomb3_coor.x = random.randint(0,width-32)
                bomb3_coor.y = 92
        
        if (bomb4_coor.bottom < height):
            bomb4_coor.y -= 4

            if bomb4_coor.top < 91:
                bomb4_coor.x = random.randint(0,width-32)
                bomb4_coor.y = height-33

        if score > 9:
            whale = pygame.image.load("whale64.png")
            speed = 4
            
            if y == 0:
                levelUpSound.play()
                whale_coor = whale.get_rect()
                whale_coor.topleft = (width/2,height/2)
                y += 1
                health_bar.hp += 20

            if (button[pygame.K_LEFT] or button[pygame.K_a]) and whale_coor.left > 0:
                whale_coor.x -= speed
            elif (button[pygame.K_RIGHT] or button[pygame.K_d]) and whale_coor.right < width:
                whale_coor.x += speed
            elif (button[pygame.K_UP] or button[pygame.K_w]) and whale_coor.top > 0:
                whale_coor.y -= speed
            elif (button[pygame.K_DOWN] or button[pygame.K_s]) and whale_coor.bottom < height:
                whale_coor.y += speed
        
        gameStatus = "inGame"

    elif quitButton.draw(gameScreen):
        gameOn = False


    if health_bar.hp == 0 or gameStatus == "gameOver":
        
        if p == 0:
            endSound.play()
            p += 1

        gameScreen.blit(gameBackground,(0,0))
        endTitle = endFont.render("GAME OVER!",True,(153,0,0))
        endTitle_coor = endTitle.get_rect()
        endTitle_coor.center = (width/2,(height/2)-10)

        endMsg = endFontMsg.render("Please exit the game.",True,(255,153,51))
        endMsg_coor = endMsg.get_rect()
        endMsg_coor.center = (width/2,(height/2)+40)

        gameScreen.blit(endTitle,endTitle_coor)
        gameScreen.blit(endMsg,endMsg_coor)
        gameScreen.blit(loseIcon,loseIcon_coor)
        gameStatus = "gameOver"

        if quitButton.draw(gameScreen):
            gameOn = False

    if score > 24 or gameStatus == "win":

        if w == 0:
            winSound.set_volume(100.0)
            winSound.play()
            
            w += 1

        gameScreen.blit(gameBackground,(0,0))

        winTitle = winFont.render("YOU WIN!",True,(51,255,51))
        winMsg = winFontMsg.render("Congratulations!",True,(255,255,51))

        winTitle_coor = winTitle.get_rect()
        winMsg_coor = winMsg.get_rect()

        winTitle_coor.center = (width/2,(height/2)-20)
        winMsg_coor.center = (width/2,(height/2)+30)

        gameScreen.blit(winTitle,winTitle_coor)
        gameScreen.blit(winMsg,winMsg_coor)
        gameScreen.blit(winIcon,winIcon_coor)
        gameStatus = "win"

        if quitButton.draw(gameScreen):
            gameOn = False

    if pygame.key.get_pressed()[pygame.K_SPACE] or gameStatus == "paused":
        gameScreen.blit(gameBackground,(0,0))
        gameStatus = "paused"

        pauseTitle = pauseFont.render("Game Paused",True,(255,128,0))
        pauseTitle_coor = pauseTitle.get_rect()
        pauseTitle_coor.center = (width/2,(height/2)-100)

        gameScreen.blit(pauseTitle,pauseTitle_coor)

        if continueButton.draw(gameScreen):
            gameStatus = "inGame"

        elif quitButton.draw(gameScreen):
            gameOn = False


    for status in pygame.event.get():
        if status.type == pygame.QUIT:
            gameOn = False
    
    
    pygame.display.update()
    time.tick(fps)