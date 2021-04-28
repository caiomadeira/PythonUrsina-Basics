from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from player import Hand
from window import Screen
from scenary import Floor, sky_set

app = Ursina()


def update():
    if held_keys['left mouse']:
        hand.aim()
    else:
        hand.with_gun()

    if held_keys['right mouse']:
        hand.shoot()

    if held_keys['q']:
        quit()

    if held_keys['2']:
        hand.with_gun()


if __name__ == '__main__':
    # init first person
    player = FirstPersonController()

    # init sky
    sky_set()

    # init floor
    for z in range(20):
        for x in range(20):
            Floor(position=(x, -20, z))

    hand = Hand()
    win = Screen()
    win.setting()
    win.text()
    app.run()
