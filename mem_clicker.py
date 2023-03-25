from pygame import *
mixer.init()
font.init()
font1 = font.SysFont("Arial", 16)
font2 = font.SysFont("Arial", 25)
 
back = transform.scale(image.load('other/back.jpg'), (500, 500))
 
counter = 1000
 
money = 0
minus = 1
 
 
 
 
win = display.set_mode((500, 500))
display.set_caption("МЕМ_КЛИКЕР_СИМУЛЯТОР")
display.set_icon(image.load("other/icon.bmp"))
clock = time.Clock()
FPS = 144
game = True
 
 
mixer.music.load('other/backmusic.ogg')
mixer.music.set_volume(0.2)
mixer.music.play()
 
 
 
 
 
 
shrekpoop = mixer.Sound('shrek/shrek.ogg')
huggypoop = mixer.Sound('huggy/huggy.ogg')
ugandapoop = mixer.Sound('uganda/uganda.ogg')
 
 
 
huggypoop.set_volume(0.1)
shrekpoop.set_volume(0.1)
ugandapoop.set_volume(0.1)
 
buysound = mixer.Sound('other/buysound.ogg')
buysound.set_volume(0.1)
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, wid=400, hei=400):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wid, hei))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
 
 
Huggy = GameSprite(player_image='huggy/huggy.png', player_x = 0, player_y=0)
Shrek = GameSprite(player_image='shrek/shrek.png', player_x = 0, player_y=0)
Uganda = GameSprite(player_image='uganda/uganda.png', player_x=0, player_y=0)
 
 
 
huggyboss = True
shrekboss = False
ugandaboss = False
 
 
 
shop = GameSprite(player_image='other/shop.png', player_x=400, player_y=0, wid=100, hei=500)
 
while game:
    win.blit(back, (0, 0))
 
    money_view = font2.render('Money:'+str(money), True, (0, 0, 0))
    win.blit(money_view, (10, 420))    
 
    minus_view = font2.render('-HP:'+str(minus), True, (0, 0, 0))
    win.blit(minus_view, (10, 460))   
 
    shop.reset()
 
    if huggyboss:
 
        Huggy.reset()
        Huggy.image = transform.scale(image.load('huggy/huggy.png'), (400, 400))
        counter_view = font1.render('HP:'+str(counter), True, (0, 0, 0))
        win.blit(counter_view, (10, 10))
 
 
 
        for e in event.get(): 
            if e.type == MOUSEBUTTONDOWN and e.button == 1: 
                x, y = e.pos 
                if Huggy.rect.collidepoint(x, y):
                    huggypoop.play()
                    counter -= minus
                    money += 1
                    Huggy.image = transform.scale(image.load('huggy/huggyclick.png'), (400, 400))
 
                if shop.rect.collidepoint(x, y) and money >= 100:
                    money -= 100
                    minus += 1
                    buysound.play()
 
 
            if e.type == QUIT:
                quit()
 
 
        if counter <= 0:
            counter = 2000 
            money += 50
            huggyboss = False
            shrekboss = True        
 
 
    if shrekboss:
 
        Shrek.reset()
        Shrek.image = transform.scale(image.load('shrek/shrek.png'), (400, 400))
        counter_view = font1.render('HP:'+str(counter), True, (0, 0, 0))
        win.blit(counter_view, (10, 10))
 
 
 
        for e in event.get(): 
            if e.type == MOUSEBUTTONDOWN and e.button == 1: 
                x, y = e.pos 
 
                if Shrek.rect.collidepoint(x, y):
                    shrekpoop.play()
                    counter -= minus
                    money += 1
                    Shrek.image = transform.scale(image.load('shrek/shrekclick.png'), (400, 400))
 
                if shop.rect.collidepoint(x, y) and money >= 100:
                    money -= 100
                    minus += 1
                    buysound.play()   
 
            if e.type == QUIT:
                quit()
 
 
 
        if counter <= 0:
            counter = 1500
            money += 50
            shrekboss = False
            ugandaboss = True 
 
 
 
    if ugandaboss:
 
        Uganda.reset()
        Uganda.image = transform.scale(image.load('uganda/uganda.png'), (400, 400))
        counter_view = font1.render('HP:'+str(counter), True, (0, 0, 0))
        win.blit(counter_view, (10, 10))
 
 
 
        for e in event.get(): 
            if e.type == MOUSEBUTTONDOWN and e.button == 1: 
                x, y = e.pos 
 
                if Uganda.rect.collidepoint(x, y):
                    ugandapoop.play()
                    counter -= minus
                    money += 1
                    Uganda.image = transform.scale(image.load('uganda/ugandaclick.png'), (400, 400))
 
                if shop.rect.collidepoint(x, y) and money >= 100:
                    money -= 100
                    minus += 1
                    buysound.play()   
 
            if e.type == QUIT:
                quit()
 
 
 
        if counter <= 0:
            counter = 1000
            money += 50
            ugandaboss = False
            huggyboss = True 
    
    clock.tick(FPS)
    display.update()