from pathlib import Path
import argparse
import shutil


def copy_files(src, dest):
    src_path = Path(src)
    dest_path = Path(dest)

    try:
        for item in src_path.iterdir():
            if item.is_file():
                extention = item.suffix[1:]
                dest_file = dest_path / extention 
                dest_file.mkdir(parents=True, exist_ok=True) # make dir if not exist
                shutil.copy2(item, dest_file) # copy file with metadata
            elif item.is_dir():
                copy_files(item, dest_path)
    except Exception as e:
        print(f"Error: {e}")

def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями.")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()


def main():
    args = parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)  # Створюємо директорію призначення, якщо вона не існує
    copy_files(args.source, args.dest)


if __name__ == "__main__":
    main()

