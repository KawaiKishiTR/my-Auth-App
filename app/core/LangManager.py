from json import load
from os import path, listdir


class LangManager():
    lang_folder: str = "lang"

    def __init__(self, lang_folder="en") -> None:
        self.lang:dict
        self.update(lang_folder)
    
    def _load_lang(self, lang_name:str):
        path_way: str = path.join(self.lang_folder, f"{lang_name}.json")
        if path.exists(path_way):
            with open(path_way, "r", encoding="utf-8") as f:
                return load(f)
        return {}

    def translate(self, *args):
        current = self.lang
        for arg in args:
            if arg in current.keys():
                current = current[arg]
        return current if isinstance(current, str) else None
    
    def update(self, new_lang_name="en"):
        self.lang = self._load_lang("en")
        if new_lang_name != "en":
            self.lang.update(self._load_lang(new_lang_name))
    
    def _lang_list(self) -> list[str]:
        return listdir(self.lang_folder)

    
if __name__ == "__main__":
    lang = LangManager()
    print(lang.lang)