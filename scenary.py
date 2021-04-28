from ursina import *


class Floor(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene,
                         position=position,
                         model='cube',
                         origin_y=0,
                         texture='brick',
                         color=color.white,
                         highlight_color=color.lime)


def sky_set():
    Entity(parent=scene,
           model="sphere",
           texture="textures/sky.png",
           scale=100,
           position=(0, 0, 0),
           double_sided=True)
