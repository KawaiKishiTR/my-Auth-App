from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
import json

class ListeEkrani(Screen):
    def on_enter(self):
        self.ids.kutu.clear_widgets()

        with open("veri/butonlar.json", "r") as f:
            veri = json.load(f)

        for item in veri:
            buton = Button(
                text=item["text"],
                background_color=get_color_from_hex(item["renk"]) + [1],
                size_hint_y=None,
                height=50
            )
            buton.bind(on_press=self.buton_basilinca)
            self.ids.kutu.add_widget(buton)

    def buton_basilinca(self, instance):
        print(f"{instance.text} butonuna tıklandı")
