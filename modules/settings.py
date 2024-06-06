from pathlib import Path
import os.path


BASE_DIR = Path(__file__).resolve().parent.parent


UI = os.path.join(BASE_DIR, 'modules', 'ui', 'ui.json')