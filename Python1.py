# Import Library
import pygame
import random

# Initializing pygame
pygame.init()
# Screen Setup
screen = pygame.display.set_mode((800, 600))
# Title and Icon
pygame.display.set_caption("Space_Invaders@Chaso")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
# background
background = pygame.image.load("spaceinvaders_background.png")
# Speed
speed = 7
bullet_speed = 13
# player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0
player_speedX = speed

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_speedX = []
num_of_enemies = 8
for i in range(num_of_enemies):
   enemyImg.append(pygame.image.load("space-ship.png"))
   enemyX.append(random.randint(0, 735))
   enemyY.append(random.randint(50, 150))
   enemyX_change.append(speed)
   enemyY_change.append(40)
   enemy_speedX.append(speed)

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"
# font
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
# game over text
over_font = pygame.font.Font("freesansbold.ttf", 80)


def show_score(x, y):
   score = font.render("Score: " + str(score_value), True, (255, 255, 255))
   screen.blit(score, (x, y))


def game_over_text():
   over_text = over_font.render("GAME OVER", True, (255, 255, 255))
   screen.blit(over_text, (200, 260))


def player(x, y):
   screen.blit(playerImg, (x, y))


def enemy(x, y, i):
   screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
   global bullet_state
   bullet_state = "fire"
   screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
   distance = ((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2) ** (1 / 2)
   if distance < 27:
       return True
   else:
       return False


# Score
score = 0

# Main Game Loop
running = True
while running:
   screen.fill((0, 0, 0))
   screen.blit(background, (0, 0))
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               playerX_change = -player_speedX
           if event.key == pygame.K_RIGHT:
               playerX_change = player_speedX
           if event.key == pygame.K_SPACE:
               if bullet_state == "ready":
                   bulletX = playerX
                   fire_bullet(playerX, bulletY)
       if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0
   playerX += playerX_change
   if playerX <= 0:
       playerX = 0
   elif playerX >= 736:
       playerX = 736
   for i in range(num_of_enemies):
       # Game Over
       if enemyY[i] > playerY - 40:
           for j in range(num_of_enemies):
               enemyY[j] = 2000
           game_over_text()
           break
       enemyX[i] += enemyX_change[i]
       if enemyX[i] <= 0:
           enemyX_change[i] = enemy_speedX[i]
           enemyY[i] += speed
       elif enemyX[i] >= 736:
           enemyX_change[i] = -speed
           enemyY[i] += enemyY_change[i]
       # Collision detection
       collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
       if collision:
           bulletY = 480
           bullet_state = "ready"
           score_value += 1
           enemyX[i] = random.randint(0, 735)
           enemyY[i] = random.randint(50, 150)
       enemy(enemyX[i], enemyY[i], i)
   if bulletY <= 0:
       bulletY = 480
       bullet_state = "ready"
   if bullet_state == "fire":
       fire_bullet(bulletX, bulletY)
       bulletY -= bullet_speed
   player(playerX, playerY)
   show_score(textX, textY)
   pygame.display.update()

