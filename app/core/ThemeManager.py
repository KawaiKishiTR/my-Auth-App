from json import load
from os import path, listdir

class ThemeManager:
    theme_folder: str = "themes"
    default_color: str = "#ff00ff"
    def __init__(self, theme_name="default") -> None:
        self.theme:dict
        self.update(theme_name)

    def _load_theme(self, theme_name):
        path_way: str = path.join(self.theme_folder, f"{theme_name}.json")
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
    
    def _theme_list(self) -> list[str]:
        return listdir(self.theme_folder)

if __name__ == "__main__":
    theme = ThemeManager()
    print(theme.theme)
