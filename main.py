from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from player import Hand, gun, gun_shot
from window import Screen

app = Ursina()


def update():
    if held_keys['left mouse']:
        hand.shot()
    else:
        hand.with_gun()

    if held_keys['q']:
        quit()

    if held_keys['2']:
        hand.with_gun()


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene, position=position, model='cube', origin_y=0, texture='brick',
                         color=color.white, highlight_color=color.lime)

    def input(self, key):
        if self.hovered:
            if


Entity(parent=scene, model="sphere", texture="textures/sky.png", scale=100, position=(0, 0, 0), double_sided=True)

for z in range(20):
    for x in range(20):
        Voxel(position=(x, 0, z))

player = FirstPersonController()
hand = Hand()
win = Screen()
app.run()
