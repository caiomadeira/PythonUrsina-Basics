from ursina import *


class Screen:

    def setting(self):
        window.title = 'Bez Saturation'  # The window title
        window.borderless = True  # Show a border
        window.fullscreen = False  # Do not go Fullscreen
        window.exit_button.visible = True  # Do not show the in-game red X that loses the window
        window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter

    def text(self):
        Text.size = 0.02
        Text.default_resolution = 1080 * Text.size
        info = Text(text="Bez Saturation - v0.1.0")
        info.x = -0.5
        info.y = 0.4
        info.background = True
        info.visible = True

