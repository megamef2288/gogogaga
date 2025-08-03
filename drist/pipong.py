import pygame
pygame.init()
printer = pygame.font.SysFont(None,43)
sdfgsrg = printer.render('gogohaaha',False,'purple')
ekran =pygame.display.set_mode((1000,750))
timer=pygame.time.Clock()
arbuz =pygame.image.load('Snimok ekrana 2025-07-20 112638.png')
arbuz = pygame.transform.scale(arbuz,(34,34))
negr = pygame.image.load('Снимок экрана 2025-07-23 182900.png')
pygame.mixer.music.load('gigasoung.wav')
class Ball:
    def __init__(self,x,y,img,speed):
        self.hitbox=img.get_rect(center=(x,y))
        self.speed_x = speed
        self.speed_y = speed
        self.speed = speed
        self.img = img
    def litaling_diagonal(self):
        self.hitbox.x += self.speed_x
        self.hitbox.y += self.speed_y
        if self.hitbox.left <= 0:
            self.speed_x = self.speed
            self.hitbox.center=(500,225)
            gigasoung.set_volume(1)
            gigasoung.play()
        elif self.hitbox.right >= 1000:
            self.speed_x = -self.speed
            self.hitbox.center=(500,225)
            gigasoung.set_volume(1)
            gigasoung.play()
        if self.hitbox.top <= 0:
            self.speed_y = self.speed
        elif self.hitbox.bottom >= 750:
            self.speed_y = -self.speed
    def ottalkivanie(self):
        if self.hitbox.colliderect(oleg.hitbox) == True:
            self.speed_x = self.speed
        elif self.hitbox.colliderect(oleja.hitbox) == True:
            self.speed_x = -self.speed
class Plitka:
    def __init__(self,x,y,img,speed):
        self.hitbox=img.get_rect(center=(x,y))
        self.speed = speed
        self.img = img
    def dwigatel(self):
        #print(nopkalist[pygame.K_w])
        knopkalist = pygame.key.get_pressed()
        if knopkalist[pygame.K_w] == True:
            self.hitbox.y -= self.speed
        elif knopkalist[pygame.K_s] == True:
            self.hitbox.y += self.speed
    def autovashesuperimba228(self):
        self.hitbox.y += self.speed
        if self.hitbox.centery > ball.hitbox.centery:
            self.speed = -1
        else:
            self.speed = 1
        

timer2 = pygame.USEREVENT
pygame.time.set_timer(timer2,30000)

ball = Ball(250,250,arbuz,2)
oleg = Plitka(100,250,negr,1)
oleja= Plitka(800,250,negr,1)
stopper = False
while True:
    ekran.fill('white')
    ekran.blit(ball.img,ball.hitbox)
    ekran.blit(oleg.img,oleg.hitbox)
    ekran.blit(oleja.img,oleja.hitbox)
    if stopper == True:
        ekran.blit(sdfgsrg,(500,275))
    ball.litaling_diagonal()
    ball.ottalkivanie()
    oleg.dwigatel()
    oleja.autovashesuperimba228()
    eventlist=pygame.event.get()
    for event in eventlist:
        if event.type == 256:
            exit() 
        elif event.type ==timer2:
            stopper = True
            

    pygame.display.update()
    timer.tick(200)
