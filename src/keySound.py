from pynput import keyboard
import pygame

class keySoundController:
    def __init__(self, classifier, group_sounds):
        # """
        # classifier: function(key) -> group_name or None
        # group_sounds: dict { group_name : sound_file }
        # """
        self.classifier = classifier
        self.group_sounds = group_sounds
        self.running = False

    def start(self):
        pygame.mixer.pre_init(44100, -16, 2, 256)
        pygame.mixer.init()

        # preload sounds (CRITICAL for real-time)
        self.sounds = {
            group: pygame.mixer.Sound(path)
            for group, path in self.group_sounds.items()
        }

        self.running = True
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()

    def stop(self):
        self.running = False
        self.listener.stop()
        pygame.mixer.quit()

    def _on_press(self, key):
        if not self.running:
            return

        group = self.classifier(key)
        if group and group in self.sounds:
            self.sounds[group].play()