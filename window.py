from ursina import *


class Screen:

    def setting(self, Button):
        window.title = 'Test'  # The window title
        window.borderless = False  # Show a border
        window.fullscreen = False  # Do not go Fullscreen
        window.exit_button.visible = False  # Do not show the in-game red X that loses the window
        window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter

    def text(self):
        Text.size = 0.05
        Text.default_resolution = 1080 * Text.size
        info = Text(text="A powerful waterfall roaring on the mountains")
        info.x = -0.5
        info.y = 0.4
        info.background = True
        info.visible = True

    def input(self, key):
        if self.hovered:
            if key == 't':
                self.text()
            else:
                destroy(self)
