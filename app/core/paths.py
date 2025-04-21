import os
from kivy.utils import platform

def get_app_data_path():
    if platform == "android":
        from android.storage import app_storage_path
        return app_storage_path()
    elif platform == "ios":
        from os.path import expanduser
        return os.path.join(expanduser("~"), "Documents")
    else:
        # Desktop: Linux, Windows, macOS
        return os.path.join(os.path.expanduser("~"), ".my_kivy_app")

def asset_path(filename):
    return os.path.join(os.path.dirname(__file__), '..', 'assets', filename)
