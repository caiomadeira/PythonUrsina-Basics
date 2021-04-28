from ursina import *


def input(key):
    if key == 'enter':
        Firstentity.texture = 'cai.png'
    elif key == 'h':
        Firstentity.texture = 'fel.png'
    elif key == 'k':
        Firstentity.texture = 'fab.png'
    elif key == 'space':
        Firstentity.texture = 'texture_test_2.png'


def update():
    Firstentity.rotation_y += 50 * time.dt

    # Firstentity.position += Firstentity.forward * time.dt


app = Ursina()

Sky(texture=load_texture('sky.jpg'))

Firstentity = Entity(model='cube',

                     texture=load_texture('tia.png'),
                     position=Vec3(1, 1, 1),
                     rotation=(0, 0, 0),
                     scale=10)

EditorCamera()

app.run()
