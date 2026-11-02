from pico2d import load_image


class Grass:
    image = None
    state = 0

    def __init__(self):
        if self.image is None:
            self.image = load_image('grass.png')
        else:
            self.state = 1

    def draw(self):
        if self.state == 0:
            self.image.draw(400, 30)
        elif self.state == 1:
            self.image.draw(400, 50)

    def update(self):
        pass
