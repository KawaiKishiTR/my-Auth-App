from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import Screen

class Ayarlar(Screen):

    def tema_degistir(self, secim):
        print(secim)
        app = App.get_running_app()
        app.theme.update(secim)
        self.ids.tema_label.text = f"Geçerli tema: {secim}"
        self._temayi_uygula()

    def _temayi_uygula(self):
        renk = App.get_running_app().theme.color("arka_plan")

        # Canvas'ı temizle
        self.ids.ana_kutu.canvas.before.clear()

        # Yeni arka planı uygula
        with self.ids.ana_kutu.canvas.before:
            print(*get_color_from_hex(renk))
            color = Color(*get_color_from_hex(renk))
            rect = Rectangle(pos=self.ids.ana_kutu.pos, size=self.ids.ana_kutu.size)

        # Referansları sakla ki silinmesin
        self._bg_color = color
        self._bg_rect = rect

        # Dinamik boyut güncellemesi için bind
        self.ids.ana_kutu.bind(pos=self._guncelle_bg, size=self._guncelle_bg)

    def _guncelle_bg(self, instance, value):
        if hasattr(self, '_bg_rect'):
            self._bg_rect.pos = instance.pos
            self._bg_rect.size = instance.size


    def _get_theme_list(self):
        app = App.get_running_app()
        return [var[:-5] for var in app.theme._theme_list()]
