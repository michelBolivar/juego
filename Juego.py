import pygame,random

from pygame.locals import *

#Definicion de constantes
WIDTH = 800
HEIGHT = 600
BLACK=(0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

pygame.init()
pygame.mixer.init()
#Creacion de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
#Controlamos los Frames por segundo
clock= pygame.time.Clock()

#Función para dibujar texto de puntaje
def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

#Función para dibujar el porcentaje de vida
def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)





## ----------------- CLASE JUGADOR ----------------------#

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert()
        #Remover el fondo negro de la imagen
        self.image.set_colorkey(BLACK)
		#-Obtiene el rectángulo delimitador de la imagen y lo asigna a la variable
        self.rect = self.image.get_rect()
		#Establece la posición horizontal del rectángulo del jugador en el centro de la pantalla.
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        #Velocidad
		#Inicializa la velocidad horizontal del jugador en 0.
        self.speed_x = 0
		# Inicializa el valor del escudo del jugador en 100
        self.shield= 100
    #Actualiza el estado del jugador en cada actualización del juego.
    def update(self):
		#Reinicia la velocidad horizontal del jugador a 0 en cada actualización.
        self.speed_x = 0
        #Captura el estado de las teclas presionadas en cada actualización.
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        #NO SALIR DE LA PANTALLA
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

#El método shoot se utiliza para que el jugador dispare una bala.
    def shoot(self):
		# Crea un objeto Bullet (bala) con la posición inicial en el centro horizontal del jugador y en la parte superior del jugador.
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        laser_sound.play()


## -------------- CLASE METEORO-------------------------------##
class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/meteorGrey_med1.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

## Se actualiza de posición en cada fotograma del juego
	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 :
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)


## ------------ CLASE BALA -----------------------##
class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/laser1.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

## Se  actualiza la posición de la bala en cada fotograma del juego
	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()


##----------------CLASE EXPLOCION ----------------------#

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
        #Cuanto tiempo espera para el siguiente cuadro velocidad de la explosión
		self.frame_rate = 50 #Velocidad de la explosión

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
                #Cundo se llega al final de la animación no se continua
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center


def show_go_screen():
	screen.blit(background, [0, 0])
	draw_text(screen, "Space Defender", 65, WIDTH // 2, HEIGHT / 4)
	draw_text(screen, "Laura Michel Bolivar", 27, WIDTH // 2, HEIGHT // 2)
	draw_text(screen, "Presiona la tecla para empezar", 17, WIDTH // 2, HEIGHT * 3/4)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False
##---------------- Imagenes -----------------------------------------------
meteor_images = []
meteor_list = ["assets/meteorGrey_big1.png", "assets/meteorGrey_big2.png", "assets/meteorGrey_big3.png", "assets/meteorGrey_big4.png",
				"assets/meteorGrey_med1.png", "assets/meteorGrey_med2.png", "assets/meteorGrey_small1.png", "assets/meteorGrey_small2.png",
				"assets/meteorGrey_tiny1.png", "assets/meteorGrey_tiny2.png"]
for img in meteor_list:
	meteor_images.append(pygame.image.load(img).convert())


##-----------------ANIMACION DE EXPLOCION ---------------------------#
explosion_anim = []
for i in range(9):
	file = "assets/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70, 70))
	explosion_anim.append(img_scale)

## ---------------------SONIDOS -------------------------------#
#Sonido del laser
laser_sound = pygame.mixer.Sound("assets/laser5.ogg")
#Sonido de la explocion con los meteoritos
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
#Musica de Fondo
pygame.mixer.music.load("assets/music.ogg")
pygame.mixer.music.set_volume(0.1)

#IMAGEN DE FONDO
background = pygame.image.load("assets/background.png").convert()



##------------- GAME OVER-------------------------------#
game_over = True
pygame.mixer.music.play(loops=-1)
# Game Loop
running = True
while running:
    # Keep loop running at the right speed
    if game_over:
        show_go_screen()
        game_over = False
        ##------------- CREACION DE LISTAS ----------------------------------------##
        all_sprites = pygame.sprite.Group()
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()

        ## ----------- CREACION DE INSTANCIAS ------------------------------------##
        player = Player()
        all_sprites.add(player)

        for i in range(8):
            meteor = Meteor()
            all_sprites.add(meteor)
            meteor_list.add(meteor)

        score = 0

    clock.tick(60)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()
    # Colisiones meteoro - laser
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
        #Se incrementa 10 puntos por cada explosión de meteoro
        score += 10
        # Sonido de la explosión
        explosion_sound.play()
        #Animación de la explosión
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        #Se generan mas meteoros
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)

    # Colisiones jugador - meteoro
    hits = pygame.sprite.spritecollide(player, meteor_list, True)
    for hit in hits:
        #Descuanta 50 puntos cada vez que el meteorito impacte la nave
        player.shield -= 25
        #Los meteoros se regeneran
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)
        if player.shield <=0:
            game_over = True
    # Draw / Render
    screen.blit(background, [0, 0])
    all_sprites.draw(screen)

    #Puntuacion
    draw_text(screen, str(score), 25, WIDTH // 2, 10)

    #Escudo

    draw_shield_bar(screen,5,5,player.shield)

    # *after* drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()