from kivy.event import EventDispatcher
from kivy.properties import DictProperty

class SharedState(EventDispatcher):
    theme_data = DictProperty({})
    lang_data = DictProperty({})

    def update_theme(self, key, value):
        self.theme_data[key] = value

    def update_lang(self, key, value):
        self.lang_data[key] = value
