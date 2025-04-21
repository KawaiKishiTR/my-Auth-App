from json import load
from os import path

class ThemeManager:
    theme_folder = "themes"
    default_color = "#ff00ff"
    def __init__(self, tema_adi="default"):
        self.theme:dict
        self.update(tema_adi)

    def _load_theme(self, ad):
        path_way = path.join(self.theme_folder, f"{ad}.json")
        if path.exists(path_way):
            with open(path_way, "r", encoding="utf-8") as f:
                return load(f)
        return {}

    def color(self, key:str):
        if key in self.theme:
            return self.theme[key]
        print(f"[UYARI] Tema dosyasında '{key}' tanımlı değil. Varsayılan renk kullanıldı.") #TODO: logging kullan
        return self.default_color

    def __getitem__(self, key):
        return self.color(key)

    def update(self, new_theme_name="default"):
        self.theme = self._load_theme("default")
        if new_theme_name != "default":
            self.theme.update(self._load_theme(new_theme_name))

if __name__ == "__main__":
    theme = ThemeManager()
    print(theme.theme)
