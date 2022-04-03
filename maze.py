from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (40, 40))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
        self.direction = "left"
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y,  wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

wh1 = Wall(30, 144, 255, 0, 10, 600, 20)
wh2 = Wall(30, 144, 255, 400, 85, 100, 20)
wh3 = Wall(30, 144, 255, 300, 170, 100, 20)
wh4 = Wall(30, 144, 255,400, 255, 100, 20)
wh5 = Wall(30, 144, 255, 0, 85, 100, 20)
wh6 = Wall(30, 144, 255, 0, 170, 200, 20)
wh7 = Wall(30, 144, 255, 0, 425, 100, 20)
wh8 = Wall(30, 144, 255, 200, 255, 100, 20)
wh9 = Wall(30, 144, 255, 200, 425, 100, 20)
wh10 = Wall(30, 144, 255, 400, 425, 200, 20)
wh11 = Wall(30, 144, 255, 0, 510, 400, 20)
wh12 = Wall(30, 144, 255, 500, 510, 100, 20)
wh13 = Wall(30, 144, 255, 300, 335, 200, 20)

ww1 = Wall(30, 144, 255, 0, 20, 20, 85)
ww2 = Wall(30, 144, 255, 300, 20, 20, 255)
ww3 = Wall(30, 144, 255, 580, 10, 20, 520)
ww4 = Wall(30, 144, 255, 500, 85, 20, 270)
ww5 = Wall(30, 144, 255, 300, 350, 20, 170)
ww6 = Wall(30, 144, 255, 100, 245, 20, 200)
ww7 = Wall(30, 144, 255, 180, 85, 20, 85)
ww8 = Wall(30, 144, 255, 0, 170, 20, 340)
ww9 = Wall(30, 144, 255, 200, 260, 20, 100)




finish = False

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.x < 755:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y < 605:
            self.rect.y += self.speed

class Enemy(GameSprite):
    
    def update(self):
        # self.direction = "left"
        if self.rect.x <=400:
            self.direction = "right"
        if self.rect.x >= 500:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#создай окно игры
win = display.set_mode((800, 650))
display.set_caption("Кега")

#задай фон сцены
backgrond = transform.scale(image.load("background.jpg"), (800, 650))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")

player = Player("hero.png", 10, 120, 5)
enemy = Enemy("cyborg.png", 400, 500, 2)
cheese = GameSprite("treasure.png", 540, 610, 0)


FPS = 30

clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        win.blit(backgrond,(0, 0))
        player.reset()
        player.update()
        enemy.reset()
        enemy.update()    
        cheese.reset()
        wh1.draw_wall()
        wh2.draw_wall()
        wh3.draw_wall()
        wh4.draw_wall()
        wh5.draw_wall()
        wh6.draw_wall()
        wh7.draw_wall()
        wh8.draw_wall()
        wh9.draw_wall()
        wh10.draw_wall()
        wh11.draw_wall()
        wh12.draw_wall()
        wh13.draw_wall()

        ww1.draw_wall()
        ww2.draw_wall()
        ww3.draw_wall()
        ww4.draw_wall()
        ww5.draw_wall()
        ww6.draw_wall()
        ww7.draw_wall()
        ww8.draw_wall()
        ww9.draw_wall()
        if sprite.collide_rect(player, cheese):
            finish = True
            mixer.music.stop()
            money.play()
        if sprite.collide_rect(player, enemy):
            finish = True
            mixer.music.stop()
            kick.play()
        if sprite.collide_rect(player, wh1) or sprite.collide_rect(player, wh2) or sprite.collide_rect(player, wh3) or sprite.collide_rect(player, wh4) or sprite.collide_rect(player, wh5) or sprite.collide_rect(player, wh6) or sprite.collide_rect(player, wh7) or sprite.collide_rect(player, wh8) or sprite.collide_rect(player, wh9) or sprite.collide_rect(player, wh10) or sprite.collide_rect(player, wh11) or sprite.collide_rect(player, wh12) or sprite.collide_rect(player, wh13) or sprite.collide_rect(player, ww1) or sprite.collide_rect(player, ww2) or sprite.collide_rect(player, ww3) or sprite.collide_rect(player, ww4) or sprite.collide_rect(player, ww5) or sprite.collide_rect(player, ww6) or sprite.collide_rect(player, ww7) or sprite.collide_rect(player, ww8) or sprite.collide_rect(player, ww9):
            finish = True
        display.update()
    clock.tick(FPS)        
#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"