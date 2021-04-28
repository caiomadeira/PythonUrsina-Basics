from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
gun = False
gun_shot = False


class Hand(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui, model='models/player/hand_empty.obj', scale=0.2, position=Vec2(0.406, -0.42),
                         texture='models/player/hand_empty.png', rotation=Vec3(0, 55, 60))

    def no_gun(self):
        self.scale = 0.2
        self.position = Vec2(0.406, -0.42)
        self.rotation = Vec3(0, 55, 60)
        self.model = 'models/player/hand_empty.obj'
        self.texture = 'models/player/hand_empty.png'

    def with_gun(self):
        self.scale = 0.2
        self.position = Vec2(0.406, -0.42)
        self.rotation = Vec3(0, 55, 60)
        self.model = 'models/player/hand_gun.obj'
        self.texture = 'models/player/hand_gun.png'

    def aim(self):
        self.scale = 0.3
        self.position = Vec2(0.69, -0.70)
        self.rotation = Vec3(0, 65, 5)
        self.model = 'models/player/hand_gun.obj'
        self.texture = 'models/player/hand_gun.png'

    def shoot(self):
        self.scale = 0.3
        self.position = Vec2(0.69, -0.70)
        self.rotation = Vec3(0, 65, 5)
        self.model = 'models/player/hand_gun_shoot.obj'
        self.texture = 'models/player/hand_gun_shoot.png'








