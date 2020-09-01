from pygame import mixer
import os


class Audio:
    def __init__(self):
        self.base_path = 'data'

    def background_music(self):
        mixer.music.load(self.get_path('background.mp3'))
        mixer.music.set_volume(.04)
        mixer.music.play(-1)

    def select_cell(self):
        sound = mixer.Sound(self.get_path('cell_select.wav'))
        sound.set_volume(.02)
        sound.play()

    def get_path(self, filename):
        return os.path.join(self.base_path, filename)
