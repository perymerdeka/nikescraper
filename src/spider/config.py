from os.path import join
from pathlib import Path

class Config(object):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    LOGDIR = join(BASE_DIR, "log")
    TEMP_DIR = join(BASE_DIR, "temp")
