import pygame, random

score = 0
scoreincrease = 1

pygame.init()
pygame.font.init()

sWidth = 395
sHeight = 600

screen = pygame.display.set_mode((sWidth, sHeight))
pygame.display.set_caption('Jump!')

clock = pygame.time.Clock()
fps = 60

font = pygame.font.Font(None, 36)

SCROLLTHRESH = 350
GRAVITY = 0.75
moving = False
scroll = 0
bgScroll = 0
speed = 2
MAXROCKETS = 4
numLives = 4
start = 0
nextcheckpoint = 200
choice = 0
Level = 1

backgroundSP = pygame.image.load("graphics/background3.png").convert()
backgroundSK = pygame.image.load("graphics/background2.png").convert()
player_image = pygame.image.load("graphics/player_walk_1s2.png").convert()
jump_image = pygame.image.load("graphics/jumpp.png").convert()
rocketplatform = pygame.image.load("graphics/rocket.png").convert()
planeplatform = pygame.image.load("graphics/plane.png").convert()
heart_image = pygame.image.load("graphics/heart.png").convert()
noheart_image = pygame.image.load("graphics/noHeart.png").convert() 
star = pygame.image.load("graphics/star.png").convert()
rain = pygame.image.load("graphics/rain.png").convert()
endscreen = pygame.image.load("graphics/GameOver2.png").convert()
hintscreen = pygame.image.load("graphics/HINTS2.png").convert()
startscreen = pygame.image.load("graphics/START.png").convert()

def drawBgSK(bgScroll):
  screen.blit(backgroundSK, (0,0 + bgScroll))
  screen.blit(backgroundSK, (0,-600 + bgScroll))

def drawBgSP(bgScroll):
  screen.blit(backgroundSP, (0,0 + bgScroll))
  screen.blit(backgroundSP, (0,-600 + bgScroll))

noheart_image = pygame.transform.scale(noheart_image, (60, 60))
heart_image = pygame.transform.scale(heart_image, (60, 60))
rocketplatform = pygame.transform.scale(rocketplatform, (90, 20))
planeplatform = pygame.transform.scale(planeplatform, (90, 30))
jump_image = pygame.transform.scale(jump_image, (50, 65))

platType = ()

class Player():
  def __init__ (self, x, y):
    self.image = player_image
    self.width = 50
    self.height = 65
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = (x, y)
    self.vel_y = 0
    self.flip = False

  def move(self):

    scroll = 0
    posX = 0
    posY = 0
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
      posX -= 5
      self.flip = True
    if key[pygame.K_d]:
      posX += 5
      self.flip = False

    self.vel_y += GRAVITY
    posY += self.vel_y

    if self.rect.bottom + posY > sHeight + 200:
      posY -= 750
      self.vel_y = -16
      global numLives
      numLives -= 1
      print(numLives)
    
    if self.rect.top <= SCROLLTHRESH:
      if self.vel_y < 0:
        scroll = -posY
    
    self.rect.x += posX
    self.rect.y += posY

    if self.rect.x > 370:
      self.rect.x = (-100)
    if self.rect.x < -100:
      self.rect.x = (370)
      
    return scroll

  def draw(self):
    screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect) 

class Star():
  def __init__(self, x, y):
    self.image = star
    self.width = 45
    self.height = 45
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = (x, y)
    self.flip = False
 
  def fall(self):

    posX = 0
    posY = 0
    
    if posY < 800:
      posY += 2
      posX += 0

    if posY > 790:
      posY == 0

    self.rect.x += posX
    self.rect.y += posY
  
  def draw3(self):
    screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Rain():
  def __init__(self, x, y):
    self.image = rain
    self.width = 45
    self.height = 45
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = (x, y)
    self.flip = False
 
  def fallR(self):

    posX = 0
    posY = 0
    
    if posY < 800:
      posY += 2
      posX += 0

    if posY > 790:
      posY == 0

    self.rect.x += posX
    self.rect.y += posY
    
  def draw3R(self):
    screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
  
class Plane():
  def __init__(self, x, y):
    self.image = planeplatform
    self.width = 90
    self.height = 20
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = (x, y)
    self.flip = False

  def scroll(self, scroll):
    self.rect.y += scroll
  
  def fly(self):

    posX = 0
    posY = 0
    
    if posX < 500:
      posX += speed
      posY += 0
    
    self.rect.x += posX
    self.rect.y += posY
    if self.rect.x > 500:
      self.rect.x = random.randint(-150, -90)
      self.rect.y = random.randint(50, 600)

    if self.rect.y > 600:
      self.rect.x = random.randint(-150, -90)
      self.rect.y = random.randint(50, 600)
   
  def draw2(self):
    screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect) 

class Rocket():
  def __init__(self, x, y):
    self.image = rocketplatform
    self.width = 90
    self.height = 20
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = (x, y)
    self.flip = False

  def scroll(self, scroll):
    self.rect.y += scroll
  
  def fly(self):

    posX = 0
    posY = 0
    
    if posX < 500:
      posX += speed
      posY += 0
    
    self.rect.x += posX
    self.rect.y += posY
    if self.rect.x > 500:
      self.rect.x = random.randint(-150, -90)
      self.rect.y = random.randint(50, 600)

    if self.rect.y > 600:
      self.rect.x = random.randint(-150, -90)
      self.rect.y = random.randint(50, 600)
   
  def draw2(self):
    screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect) 

character = Player(sWidth // 2, sHeight -350)

stars = []
starX = 175
starY = -450
goldStar = Star(starX, starY)
stars.append(goldStar)

rainL = []
rainX = 175
rainY = -450
rainDrop = Rain(rainX, rainY)
rainL.append(rainDrop)


platforms = []

for i in range(MAXROCKETS):
  platform = Rocket((random.randint(-100, 600)), (random.randint(50, 650)))
  platforms.append(platform)

play = True  
while play == True:
  if choice == 1:
    drawBgSK(bgScroll)
    Level == 1
  elif choice == 2:
    drawBgSP(bgScroll)
    Level == 2
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
  
  for i in platforms:
    collide = pygame.Rect.colliderect(character.rect, i.rect)
    if collide:
      if ((character.rect.y + 30 > i.rect.y - 10) and (character.rect.y < i.rect.y + 10)):
        if character.vel_y > 0:
          character.vel_y = -18

  for i in stars:
    collision = pygame.Rect.colliderect(character.rect, i.rect)
    if collision:
      scoreUp = 0
      if scoreUp != 500:
        score += 10
      nextcheckpoint += 10

  for i in rainL:
    collisionR = pygame.Rect.colliderect(character.rect, i.rect)
    if collisionR:
      scoreUpR = 0
      if scoreUpR != 500:
        score += 10
      nextcheckpoint += 10
      
  clock.tick(fps)
  if numLives >= 0 and numLives < 4:
    scroll = character.move()

  if character.rect.y <200:
    score += scoreincrease

  bgScroll += scroll  
  if bgScroll >= 600:
    bgScroll = 0
  
  score_text = font.render(f'Score: {score}', True, (255, 255, 255))
  screen.blit(score_text, (10, 10))
  sChoice = pygame.key.get_pressed()
  if numLives == 4:
    platforms.clear()
    stars.clear()
    rainL.clear()
    start == 0
    screen.blit(startscreen, (0, 0))
    
    if sChoice[pygame.K_q]:
      pygame.quit()
    if sChoice[pygame.K_1]:
      choice = 1
      print("b")
      numLives -= 1
      print (numLives)
      rainL.append(rainDrop)
      platform1 = Plane(200, 600)
      platforms.append(platform1)
      for i in range(MAXROCKETS):
        platform = Plane((random.randint(-100, 600)), (random.randint(50, 650)))
        platforms.append(platform)
      
    if sChoice[pygame.K_2]:
      choice = 2
      print("a")
      numLives -= 1
      print (numLives)
      stars.append(goldStar)
      platform1 = Rocket(200, 600)
      platforms.append(platform1)
      for i in range(MAXROCKETS):
        platform = Rocket((random.randint(-100, 600)), (random.randint(50, 650)))
        platforms.append(platform)
      
  elif numLives == 3:
    
    screen.blit(heart_image, (250, 5))
    screen.blit(heart_image, (285, 5))
    screen.blit(heart_image, (320, 5))

  elif numLives == 2:
    screen.blit(noheart_image, (250, 5))
    screen.blit(heart_image, (285, 5))
    screen.blit(heart_image, (320, 5))

  elif numLives == 1:
    screen.blit(noheart_image, (250, 5))
    screen.blit(noheart_image, (285, 5))
    screen.blit(heart_image, (320, 5))

  elif numLives == 0:
    screen.blit(noheart_image, (250, 5))
    screen.blit(noheart_image, (285, 5))
    screen.blit(noheart_image, (320, 5))

  elif numLives <= -1:
    platforms.clear()
    stars.clear()
    rainL.clear()
    screen.blit(endscreen, (0, 0))
    choice = pygame.key.get_pressed()
    
    if choice[pygame.K_q]:
      pygame.quit()
      
    if choice[pygame.K_r]:
      score -= score
      numLives += 5
      nextcheckpoint == 200
      print(numLives)
      stars.append(goldStar)
      platforms.append(platform1)
      for i in range(MAXROCKETS):
        platform = Rocket((random.randint(-100, 600)), (random.randint(50, 650)))
        platforms.append(platform)

    if choice[pygame.K_h]:
      screen.blit(hintscreen, (0, 0))

  if numLives >= 0 and numLives < 4:
    character.draw()

  if score >= nextcheckpoint:
    for i in stars:
      i.fall()
      i.draw3()
      
  if score >= nextcheckpoint:
    for i in rainL:
      i.fallR()
      i.draw3R()

  if numLives >= 0 and numLives < 4:
    for i in platforms:
      i.fly()
      i.scroll(scroll)
      i.draw2()

  pygame.display.update()
