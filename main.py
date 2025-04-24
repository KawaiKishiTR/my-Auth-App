from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from app.screens.ana_ekran import AnaEkran
from app.screens.ayarlar import Ayarlar
from os import listdir
from app.core.SharedState import SharedState

for file in listdir("app/KV_files"):
    if file.endswith(".kv"):
        Builder.load_file("app/KV_files/" + file)


class UygulamaYonetici(ScreenManager):
    pass

class Uygulama(App):
    def build(self):
        self.shared_data = SharedState()
        return UygulamaYonetici()

if __name__ == '__main__':
    Uygulama().run()
