from background_task import background
from .api import hardupdate

@background()
def start():
    hardupdate()
    