from pathlib import Path

DATA_PATH = Path.cwd() / 'data'

DB_PATH = DATA_PATH / 'data.db'

CONTENT_AGREGATOR_DB =  'sqlite+aiosqlite:///' + str(DB_PATH)