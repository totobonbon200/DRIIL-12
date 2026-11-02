from pico2d import load_image

class Grass:
    image = None
    state = 0

    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        if self.state == 0:
            self.image.draw(400, 50)
        elif self.state == 1:
            self.image.draw(400, 30)

    def update(self):
        pass
