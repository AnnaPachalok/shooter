from pygame import*

init()

W, H = 500, 700
window = display.set_mode((W, H))
display.set_caption("shooter")
display.set_icon(image.load("images/ufo.png"))

bg = transform.scale(image.load("images/galaxy.jpg"), (W, H))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, width, height, speed, img):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    pass

player = Player(W / 2, H - 100, 50, 100, 10, "images/rocket.png")


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(bg, (0, 0))
    player.draw()
    display.update()
    clock.tick(60)
