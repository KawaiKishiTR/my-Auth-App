from kivy.app import App
from kivy.uix.screenmanager import Screen

class BaseScreen(Screen):
    def on_enter(self):
        state = App.get_running_app().shared_data
        state.bind(theme_data=self.on_theme_change)
        state.bind(lang_data=self.on_lang_change)

        # İlk yükleme için hemen tetikle
        self.on_theme_change(state, state.theme_data)
        self.on_lang_change(state, state.lang_data)

    def on_theme_change(self, instance, theme):
        # Tema güncellendiğinde yapılacaklar
        pass

    def on_lang_change(self, instance, lang):
        # Dil güncellendiğinde yapılacaklar
        pass
