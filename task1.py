"""
    Написать скрипт, который будет рекурсивно выводить содержимое текущей директории
        до 2 уровня глубины (аналог unix утилиты tree ---> tree -L 2).

    Подсказка: используйте from pathlib import Path.
    Пример работы скрипта на данном репозитории
"""
from pathlib import Path

# 0 - текущая папка, 1 - вложенные и тд

def print_tree(root_path: Path, prefix: str = "", max_depth: int = 2, current_depth: int = 0):
    if current_depth > max_depth:
        return

    try:
        contents = sorted(root_path.iterdir(), key=lambda x: (x.is_file(), x.name))
    except PermissionError:
        print(f'{prefix}└── [Нет доступа]')
        return

    total = len(contents)
    for i, path in enumerate(contents):
        is_last = (i == total - 1)
        connector = "└── " if is_last else "├── "

        print(f'{prefix}{connector}{path.name}')

        if path.is_dir():
            extension = "   " if is_last else "│   "
            new_prefix = prefix + extension
            print_tree(path, new_prefix, max_depth, current_depth + 1)

if __name__ == '__main__':
    current_dir = Path('.')
    print(current_dir.resolve())
    print_tree(current_dir, max_depth=2)
