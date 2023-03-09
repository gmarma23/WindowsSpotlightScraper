import os


USER_ROOT_DIR = os.path.expanduser('~')
USER_PICTURES_DIR = os.path.join(USER_ROOT_DIR, 'Pictures')
USER_DOWNLOADS_DIR = os.path.join(USER_ROOT_DIR, 'Downloads')


def create_dir_path(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def sanitize_filename(filename: str) -> None:
    for ch in ['\\','/','<','>',':','\"','|','?','*']:
        if ch in filename:
            filename.replace(ch, '')
            