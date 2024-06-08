import os

PROJECT_DIR = os.getcwd()  # カレントディレクトリを取得
SETTINGS_FILE = 'settings.txt'

print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE))
