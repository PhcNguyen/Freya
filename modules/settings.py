from pathlib import Path
import os.path


BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False

UI = os.path.join(BASE_DIR, 'modules', 'ui', 'ui.json')
PATH_VERSION = os.path.join(BASE_DIR, 'modules', '.version')

ERROR_MESSAGE = "Đã có lỗi không mong muốn xảy ra! Hãy liên hệ với Developers để khắc phục sự cố."

VERSION = open(PATH_VERSION).read().strip()

